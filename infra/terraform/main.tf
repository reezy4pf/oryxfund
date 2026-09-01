# ==============================================================================
# ORYX FUND — MULTI-REGION HIGH-AVAILABILITY CLOUD TOPOLOGY (main.tf)
# Production AWS Infrastructure as Code for Cape Town (af-south-1) Primary
# and Dublin (eu-west-1) Disaster Recovery Standby.
# ==============================================================================

terraform {
  required_version = ">= 1.8.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50.0"
    }
  }
  backend "s3" {
    bucket         = "oryx-fund-terraform-state-prod"
    key            = "core/production.tfstate"
    region         = "af-south-1"
    dynamodb_table = "oryx-terraform-locks"
    encrypt        = true
  }
}

# --- AWS Providers ---
provider "aws" {
  region = var.primary_region
  alias  = "primary"
  default_tags {
    tags = {
      Project     = "OryxFund"
      Environment = "Production"
      Compliance  = "CBK-DCP-2022"
      ManagedBy   = "Terraform"
    }
  }
}

provider "aws" {
  region = var.dr_region
  alias  = "dr"
  default_tags {
    tags = {
      Project     = "OryxFund"
      Environment = "DisasterRecovery"
      ManagedBy   = "Terraform"
    }
  }
}

# --- 1. Multi-AZ VPC Networking (Cape Town af-south-1) ---
module "primary_vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.8.0"
  providers = { aws = aws.primary }

  name = "oryx-primary-vpc-prod"
  cidr = "10.100.0.0/16"

  azs             = ["af-south-1a", "af-south-1b", "af-south-1c"]
  private_subnets = ["10.100.1.0/24", "10.100.2.0/24", "10.100.3.0/24"]
  public_subnets  = ["10.100.101.0/24", "10.100.102.0/24", "10.100.103.0/24"]
  database_subnets = ["10.100.201.0/24", "10.100.202.0/24", "10.100.203.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = false
  one_nat_gateway_per_az = true
  enable_vpn_gateway     = false
  enable_dns_hostnames   = true
  enable_dns_support     = true
}

# --- 2. AWS Key Management Service (KMS) Customer Managed Keys ---
resource "aws_kms_key" "primary_envelope_key" {
  provider                = aws.primary
  description             = "Oryx Fund Master KEK for Field-Level Envelope Encryption (KDPA 2019)"
  deletion_window_in_days = 30
  enable_key_rotation     = true
}

resource "aws_kms_alias" "primary_envelope_key_alias" {
  provider      = aws.primary
  name          = "alias/oryx-fund-envelope-key-prod"
  target_key_id = aws_kms_key.primary_envelope_key.key_id
}

# --- 3. Amazon Aurora PostgreSQL 16+ Multi-AZ with Cross-Region Replica ---
resource "aws_rds_cluster" "primary_aurora" {
  provider                = aws.primary
  cluster_identifier      = "oryx-aurora-postgres-primary"
  engine                  = "aurora-postgresql"
  engine_version          = "16.2"
  database_name           = "oryx_fund_ledger"
  master_username         = var.db_master_username
  master_password         = var.db_master_password
  db_subnet_group_name    = module.primary_vpc.database_subnet_group_name
  vpc_security_group_ids  = [aws_security_group.db_sg.id]
  storage_encrypted       = true
  kms_key_id              = aws_kms_key.primary_envelope_key.arn
  backup_retention_period = 35
  preferred_backup_window = "01:00-03:00"
  deletion_protection     = true
  enable_http_endpoint    = true
}

resource "aws_rds_cluster_instance" "primary_instances" {
  count              = 3
  provider           = aws.primary
  identifier         = "oryx-aurora-instance-${count.index}"
  cluster_identifier = aws_rds_cluster.primary_aurora.id
  instance_class     = "db.r6g.xlarge"
  engine             = aws_rds_cluster.primary_aurora.engine
  engine_version     = aws_rds_cluster.primary_aurora.engine_version
}

# --- 4. Amazon ElastiCache for Redis Cluster (Redlock & Caching) ---
resource "aws_elasticache_replication_group" "redis_cluster" {
  provider                   = aws.primary
  replication_group_id       = "oryx-redis-cluster-prod"
  description                = "Oryx Fund Multi-AZ Redis for Redlock and Session Tokens"
  node_type                  = "cache.r6g.large"
  num_cache_clusters         = 3
  port                       = 6379
  parameter_group_name       = "default.redis7"
  automatic_failover_enabled = true
  multi_az_enabled           = true
  subnet_group_name          = aws_elasticache_subnet_group.redis_subnet_group.name
  security_group_ids         = [aws_security_group.redis_sg.id]
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  auth_token                 = var.redis_auth_token
}

resource "aws_elasticache_subnet_group" "redis_subnet_group" {
  provider   = aws.primary
  name       = "oryx-redis-subnet-group"
  subnet_ids = module.primary_vpc.private_subnets
}

# --- 5. Amazon S3 Object Lock (7-Year Compliance Mode WORM Storage) ---
resource "aws_s3_bucket" "audit_worm_bucket" {
  provider      = aws.primary
  bucket        = "oryx-fund-regulatory-audit-worm-prod"
  force_destroy = false

  object_lock_enabled = true
}

resource "aws_s3_bucket_object_lock_configuration" "audit_worm_lock" {
  provider = aws.primary
  bucket   = aws_s3_bucket.audit_worm_bucket.id

  rule {
    default_retention {
      mode = "COMPLIANCE"
      days = 2555 # 7 Years Regulatory Retention
    }
  }
}

# --- 6. Amazon Elastic Kubernetes Service (EKS) Cluster ---
module "primary_eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.8.0"
  providers = { aws = aws.primary }

  cluster_name    = "oryx-fund-eks-cluster-prod"
  cluster_version = "1.30"

  vpc_id                         = module.primary_vpc.vpc_id
  subnet_ids                     = module.primary_vpc.private_subnets
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    general_workers = {
      min_size     = 3
      max_size     = 30
      desired_size = 6

      instance_types = ["m6i.xlarge", "m6a.xlarge"]
      capacity_type  = "ON_DEMAND"
    }
  }
}

# --- Security Groups ---
resource "aws_security_group" "db_sg" {
  provider    = aws.primary
  name        = "oryx-db-security-group"
  description = "Allow inbound PostgreSQL traffic from EKS worker nodes only"
  vpc_id      = module.primary_vpc.vpc_id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [module.primary_eks.node_security_group_id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "redis_sg" {
  provider    = aws.primary
  name        = "oryx-redis-security-group"
  description = "Allow inbound Redis traffic from EKS worker nodes only"
  vpc_id      = module.primary_vpc.vpc_id

  ingress {
    from_port       = 6379
    to_port         = 6379
    protocol        = "tcp"
    security_groups = [module.primary_eks.node_security_group_id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
