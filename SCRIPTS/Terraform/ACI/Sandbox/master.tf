# Teraform file to make ACI changes 

terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
      version = "0.5.4"
    }
  }
}

#configure provider with your cisco aci credentials.
provider "aci" {
  # cisco-aci user name
  username = "admin"
  # cisco-aci password
  password = "password"
  # cisco-aci url
  url      = "https://my-cisco-aci.com"
  insecure = true
}

resource "aci_tenant" "test-tenant" {
  name        = "test-tenant"
  description = "This tenant was reated by terraform"
}

resource "aci_application_profile" "test-app" {
  tanent_dn   = "${aci_tenant.test-tenant.id}"
  name        = "test-app"
  description = "This app profile is created by terraform"
}