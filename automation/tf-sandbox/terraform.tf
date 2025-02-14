terraform {
  required_version = "~> 1.4.0"

  backend "s3" {
    # Store the TF state file and lock by the dynamodb 
    bucket         = "eks-fargate-demo-dev"
    key            = "terraform/eks/fargate/dev.tfstate"
    region         = "us-east-1"
    dynamodb_table = "eks-fargate-demo-dev"
    encrypt        = true
  }
}
