# ==============================================================================
# ORYX FUND — TERRAFORM OUTPUTS (outputs.tf)
# ==============================================================================

output "eks_cluster_endpoint" {
  value       = module.primary_eks.cluster_endpoint
  description = "Primary Amazon EKS Kubernetes API endpoint"
}

output "aurora_cluster_endpoint" {
  value       = aws_rds_cluster.primary_aurora.endpoint
  description = "Primary Aurora PostgreSQL master endpoint"
}

output "aurora_reader_endpoint" {
  value       = aws_rds_cluster.primary_aurora.reader_endpoint
  description = "Aurora PostgreSQL read replica endpoint for analytics"
}

output "redis_primary_endpoint" {
  value       = aws_elasticache_replication_group.redis_cluster.primary_endpoint_address
  description = "Primary Redis endpoint for Redlock distributed locking"
}

output "kms_cmk_arn" {
  value       = aws_kms_key.primary_envelope_key.arn
  description = "AWS KMS CMK ARN for Field-Level Envelope Encryption"
}

output "audit_worm_bucket_id" {
  value       = aws_s3_bucket.audit_worm_bucket.id
  description = "S3 Object Lock Compliance WORM bucket name"
}
