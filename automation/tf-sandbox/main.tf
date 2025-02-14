
# VPC
resource "aws_vpc" "eks-fargate-demo-dev" {
  cidr_block = "10.0.0.0/16"
  
  # Must be enabled for EFS
  enable_dns_hostnames = true

  enable_dns_support   = true

  tags = {
    Name = "eks-fargate-demo-dev"
  }
}

# Public Subnet
resource "aws_subnet" "eks-demo-public-01" {
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  vpc_id                  = aws_vpc.eks-fargate-demo-dev.id
  map_public_ip_on_launch = true
  tags = {
    "Name"                               = "eks-demo-public-01"
    "kubernetes.io/role/elb"             = "1"
  }
}

# Private Subnet
resource "aws_subnet" "eks-demo-private-01" {
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1a"
  vpc_id                  = aws_vpc.eks-fargate-demo-dev.id
  map_public_ip_on_launch = true
  tags = {
    "Name"                                        = "eks-demo-private-01"
    "kubernetes.io/role/internal-elb"             = "1"
  }
}

# Public Subnet
resource "aws_subnet" "eks-demo-public-02" {
  cidr_block              = "10.0.3.0/24"
  availability_zone       = "us-east-1b"
  vpc_id                  = aws_vpc.eks-fargate-demo-dev.id
  map_public_ip_on_launch = true
  tags = {
    "Name"                               = "eks-demo-public-02"
    "kubernetes.io/role/elb"             = "1"
  }
}

# Private Subnet
resource "aws_subnet" "eks-demo-private-02" {
  cidr_block              = "10.0.4.0/24"
  availability_zone       = "us-east-1b"
  vpc_id                  = aws_vpc.eks-fargate-demo-dev.id
  map_public_ip_on_launch = true
  tags = {
    "Name"                                        = "eks-demo-private-02"
    "kubernetes.io/role/internal-elb"             = "1"
  }
}

resource "aws_eip" "demo-eip-01" {
  domain                    = "vpc"
  depends_on = [aws_internet_gateway.eks-demo-internet-gateway-01]
  tags = {
    Name = "demo-eip-01"
  }
}


resource "aws_internet_gateway" "eks-demo-internet-gateway-01" {
  vpc_id = aws_vpc.eks-fargate-demo-dev.id
  tags = {
    Name = "eks-demo-internet-gateway"
  }
}


resource "aws_nat_gateway" "eks-demo-internet-nat" {
  allocation_id = aws_eip.demo-eip-01.id
  subnet_id     = aws_subnet.eks-demo-public-01.id

  tags = {
    Name = "eks-demo-net-gateway"
  }

  depends_on = [aws_internet_gateway.eks-demo-internet-gateway-01]
}


resource "aws_route_table" "eks-demo-public" {
  vpc_id = aws_vpc.eks-fargate-demo-dev.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.eks-demo-internet-gateway-01.id
  }

  tags = {
    Name = "eks-demo-public"
  }
}

resource "aws_route_table" "eks-demo-private" {
  vpc_id = aws_vpc.eks-fargate-demo-dev.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.eks-demo-internet-nat.id
  }

  tags = {
    Name = "eks-demo-private"
  }
}

resource "aws_route_table_association" "private-us-east-1a" {
  subnet_id      = aws_subnet.eks-demo-private-01.id
  route_table_id = aws_route_table.eks-demo-private.id
}


resource "aws_route_table_association" "private-us-east-1b" {
  subnet_id      = aws_subnet.eks-demo-private-02.id
  route_table_id = aws_route_table.eks-demo-private.id
}


resource "aws_route_table_association" "public-us-east-1a" {
  subnet_id      = aws_subnet.eks-demo-public-01.id
  route_table_id = aws_route_table.eks-demo-public.id
}


resource "aws_route_table_association" "public-us-east-1b" {
  subnet_id      = aws_subnet.eks-demo-public-02.id
  route_table_id = aws_route_table.eks-demo-public.id
}

resource "aws_security_group" "eks_fargate_sg" {
  vpc_id = aws_vpc.eks-fargate-demo-dev.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "eks-fargate-sg"
  }
}


# eks-cluster-01
resource "aws_eks_cluster" "eks-fargate-demo-dev" {
  name     = "eks-fargate-demo-dev"
  version  = "1.30"
  role_arn = aws_iam_role.eks-demo-cluster-admin-role-01.arn
  vpc_config {
    subnet_ids              = [
      aws_subnet.eks-demo-private-01.id,
      aws_subnet.eks-demo-private-02.id,
      aws_subnet.eks-demo-public-01.id,
      aws_subnet.eks-demo-public-02.id
      ]
    endpoint_public_access  = true
    endpoint_private_access = true
    public_access_cidrs     = ["0.0.0.0/0"]

  }
   access_config {
    authentication_mode = "API_AND_CONFIG_MAP"
    bootstrap_cluster_creator_admin_permissions = true
  }
  depends_on = [
    aws_iam_role_policy_attachment.eks-fargate-demo-dev-AmazonEKSClusterPolicy,aws_iam_role_policy_attachment.eks-fargate-demo-dev-AmazonEKSVPCResourceController
  ]
  tags = {
    demo = "eks"
  }
}

data "aws_iam_policy_document" "eks-demo-cluster-admin-role-policy" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "eks-demo-cluster-admin-role-01" {
  name               = "eks-demo-cluster-admin-role-01"
  assume_role_policy = data.aws_iam_policy_document.eks-demo-cluster-admin-role-policy.json
}

resource "aws_iam_role_policy_attachment" "eks-fargate-demo-dev-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks-demo-cluster-admin-role-01.name
}


resource "aws_iam_role_policy_attachment" "eks-fargate-demo-dev-AmazonEKSVPCResourceController" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
  role       = aws_iam_role.eks-demo-cluster-admin-role-01.name
}


# Addones
resource "aws_eks_addon" "eks-demo-addon-coredns" {
  cluster_name                = aws_eks_cluster.eks-fargate-demo-dev.name
  addon_name                  = "coredns"
  addon_version               = "v1.11.1-eksbuild.9" 
  resolve_conflicts_on_create = "OVERWRITE" 
}

resource "aws_eks_addon" "eks-demo-addon-kube-proxy" {
  cluster_name                = aws_eks_cluster.eks-fargate-demo-dev.name
  addon_name                  = "kube-proxy"
  addon_version               = "v1.30.0-eksbuild.3" 
  resolve_conflicts_on_create = "OVERWRITE" 
}

resource "aws_eks_addon" "eks-demo-addon-vpc-cni" {
  cluster_name                = aws_eks_cluster.eks-fargate-demo-dev.name
  addon_name                  = "vpc-cni"
  addon_version               = "v1.18.3-eksbuild.1" 
  resolve_conflicts_on_create = "OVERWRITE" 
}

resource "aws_iam_role" "eks-fargate-demo-profile-role-01" {
  name = "eks-fargate-demo-profile-role-01"

  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "eks-fargate-pods.amazonaws.com"
      }
    }]
    Version = "2012-10-17"
  })
}

# eks-fargate-01
resource "aws_eks_fargate_profile" "fargate-demo-01" {
  cluster_name           = aws_eks_cluster.eks-fargate-demo-dev.name
  fargate_profile_name   = "fargate-demo-01"
  pod_execution_role_arn = aws_iam_role.eks-fargate-demo-profile-role-01.arn
  subnet_ids = [
      aws_subnet.eks-demo-private-01.id,
      aws_subnet.eks-demo-private-02.id
  ]
  selector {
    namespace = "kube-system"
    labels = {
      k8s-app="kube-dns"
    }
  }
  selector {
    namespace = "demo"
  }

}

resource "aws_iam_role_policy_attachment" "eks-demo-fargate-profile-01" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy"
  role       = aws_iam_role.eks-fargate-demo-profile-role-01.name
}

