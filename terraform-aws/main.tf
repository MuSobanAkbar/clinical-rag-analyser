terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}


module "portfolio_bucket" {
  source      = "./modules/s3-bucket"
  bucket_name = "soban-devops-portfolio-2026" 
}


output "final_arn" {
  value = module.portfolio_bucket.bucket_arn
}
