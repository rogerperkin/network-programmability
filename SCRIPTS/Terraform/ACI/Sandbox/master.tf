# Teraform file to make changes to ACI

terraform {
  required_providers {
    aci = {
      source  = "CiscoDevNet/aci"
      version = "0.5.4"
    }
  }
}

#configure provider with your cisco aci credentials.
provider "aci" {
  # cisco-aci user name
  username = "admin"
  # cisco-aci password
  password = "ciscopsdt"
  # cisco-aci url
  url      = "https://sandboxapicdc.cisco.com"
  insecure = true
}
#create the Tenant 
resource "aci_tenant" "test-tenant" {
  name        = "TerraTenant"
  description = "This tenant was created by terraform"
}
#create the Application Profile 
resource "aci_application_profile" "test-app" {
  tenant_dn   = aci_tenant.test-tenant.id
  name        = "test-app"
  description = "This app profile is created by terraform"
}


