# Terraform File to configure Cisco ASA 

terraform {
  required_providers {
    ciscoasa = {
      source = "hashicorp/ciscoasa"
      version = ">= 1.2.0"
    }
  }
}
#================================================================
# Define access credentials for ASAv
#================================================================

provider "ciscoasa" {
  api_url       = "https://192.168.1.245"
  username      = "roger"
  password      = "cisco"
  ssl_no_verify = true
}

#================================================================
# static Route configuration 
#================================================================

resource "ciscoasa_static_route" "ipv4_static_route" {
  interface = "INSIDE"
  network   = "10.254.0.0/16"
  gateway   = "192.168.10.20"
}

resource "ciscoasa_static_route" "ipv4_static_route2" {
  interface = "INSIDE"
  network   = "10.253.0.0/16"
  gateway   = "192.168.10.20"
}

resource "ciscoasa_static_route" "ipv4_static_route3" {
  interface = "INSIDE"
  network   = "10.252.0.0/16"
  gateway   = "192.168.10.20"
}

resource "ciscoasa_static_route" "ipv4_static_route4" {
  interface = "INSIDE"
  network   = "10.251.0.0/16"
  gateway   = "192.168.10.20"

}

#================================================================
# ACL configuration 
#================================================================

#================================================================
# Custom config data specified in separate file tbc
#================================================================

# user_data = file("asav_config.txt")




