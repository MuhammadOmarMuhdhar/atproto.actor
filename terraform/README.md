# Infrastructure as Code

Terraform configuration for Google Cloud infrastructure provisioning.

## Terraform Files:
- `main.tf` - Core infrastructure resources (Cloud Run, Cloud SQL, Storage)
- `variables.tf` - Input variables for different environments
- `outputs.tf` - Output values for other systems and CI/CD

## Resources Managed:
- Cloud Run service for application hosting
- Cloud SQL PostgreSQL instance
- Cloud Storage buckets for static assets
- IAM roles and service accounts
- VPC and networking configuration
- Cloud Tasks queues for background jobs

## Usage:
```bash
terraform init
terraform plan -var-file="prod.tfvars"
terraform apply -var-file="prod.tfvars"
```

## Environments:
- `dev.tfvars` - Development environment configuration
- `staging.tfvars` - Staging environment configuration  
- `prod.tfvars` - Production environment configuration