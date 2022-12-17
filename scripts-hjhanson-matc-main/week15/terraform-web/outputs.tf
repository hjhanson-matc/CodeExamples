output "instance_public_ip" {
    description = "The public ip address of the EC2 instance"
    value = module.ec2_instance.public_ip
}