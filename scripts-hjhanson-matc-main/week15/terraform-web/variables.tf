variable "region" {
    type = string
    default = "us-east-1"
}
variable "Ip_Cidr" {
    type = string
    default = "10.0.0.0/16"
}
variable "Public_Subnets" {
    type = list(string)
    default = ["10.0.1.0/24","10.0.2.0/24"]
}
variable "Private_Subnets" {
    type = list(string)
    default = ["10.0.101.0/24","10.0.102.0/24"]
}