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

resource "aws_s3_bucket" "portfolio" {
  bucket = "soban-devops-portfolio-2026-bucket" 
  tags = {
    Name      = "DevOps Portfolio"
    ManagedBy = "terraform"
  }
}
