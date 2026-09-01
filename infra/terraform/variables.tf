# ==============================================================================
# ORYX FUND — TERRAFORM VARIABLES (variables.tf)
# ==============================================================================

variable "primary_region" {
  type        = string
  default     = "af-south-1"
  description = "Primary production AWS region in Cape Town, South Africa"
}

variable "dr_region" {
  type        = string
  default     = "eu-west-1"
  description = "Disaster recovery standby AWS region in Dublin, Ireland"
}

variable "db_master_username" {
  type        = string
  default     = "oryx_root_admin"
  description = "Master username for Aurora PostgreSQL cluster"
}

variable "db_master_password" {
  type        = string
  sensitive   = true
  description = "Master password for Aurora PostgreSQL cluster"
}

variable "redis_auth_token" {
  type        = string
  sensitive   = true
  description = "Authentication token for ElastiCache Redis cluster"
}
