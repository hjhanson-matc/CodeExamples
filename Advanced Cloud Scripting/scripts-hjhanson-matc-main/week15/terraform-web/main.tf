terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.27"
        }
    }

    required_version = ">= 0.14.9"
}

provider "aws" {
    profile = "default"
    region = var.region
}

data "aws_availability_zones" "available" {
    state = "available"
    filter {
        name = "region-name"
        values = ["var.region"]
    }
}

module "vpc" {
    source = "terraform-aws-modules/vpc/aws"
    name = "Lab-VPC"
    cidr = var.Ip_Cidr
    azs = ["us-east-1a","us-east-1b","us-east-1c","us-east-1d"]
    public_subnets = var.Public_Subnets
    private_subnets = var.Private_Subnets
}

module "web_server_sg" {
    source = "terraform-aws-modules/security-group/aws//modules/http-80"
    name = "web-sg"
    vpc_id = module.vpc.vpc_id
    ingress_cidr_blocks = ["0.0.0.0/0"]
}

data "aws_ami" "valid" {
    owners = ["amazon"]
    most_recent = true
    filter {
        name = "name"
        values = ["amzn2-ami-hvm-*-x86_64-gp2"]
    }
}

module "ec2_instance" {
    source = "terraform-aws-modules/ec2-instance/aws"
    version = "~> 3.0"

    name = "hunter-web-server"

    ami = data.aws_ami.valid.id
    instance_type = "t2.micro"
    key_name = "vockey"
    vpc_security_group_ids = [module.web_server_sg.security_group_id]
    subnet_id = module.vpc.public_subnets[0]
    user_data = templatefile("${path.module}/init-script.sh",{file_content="Hunter Hanson"})
    depends_on = [
        module.vpc
    ]
}