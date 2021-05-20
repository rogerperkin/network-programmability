provider "aws" {
  access_key = "var.access_key"
  secret_key = "var.secret_key"
  region     = "var.aws_region"
}

resource "aws_default_vpc" "default" {

}



resource "aws_security_group" "allow_ssh" {
  name = "automation-demo"
}

resource "aws_instance" "Ubuntu-Server" {
  ami           = "ami-096cb92bb3580c759"
  instance_type = "t2.micro"

}

variable "network_address_space" {
  default = "10.1.0.0/16"
}

