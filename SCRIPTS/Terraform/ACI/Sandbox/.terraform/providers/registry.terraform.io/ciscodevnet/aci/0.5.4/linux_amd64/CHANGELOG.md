## 0.5.4 (January 13, 2020)

BUG FIXES:
- Added Missing documentation for aci_monitoring_policy resource.

## 0.5.3 (December 22, 2020)

IMPROVEMENTS:
- Added New attribute named endpoint_path to fvcep data-source.
- Added More levels for priorities to the application_profile resource. (Supported in latest version of APIC)

BUG FIXES:
- Renamed `_from` attribute to `from` for aci_ranges resource.

BREAKING CHANGES:
- scope attribute for aci_l3_ext_subnet resource is now list of string rather than a single string. This change will break your infrastructure if you have l3extsubnet created with terraform. Consider removing the l3extsubnet resource from your terraform state file using `terraform state rm` and than run the `terraform apply` to make your configuration inline with the new changes. This will not affect the l3extsubnet which is already there.

## 0.5.2 (November 20, 2020)

BUG FIXES:
- Fixed an issue with aci_subnet ctrl attribute to have list value.
- Fixed an issue with aci_any relations being not created.
- Fixed an issue with aci_cloud_subnet to have name attribute.

## 0.5.1 (November 05, 2020)

IMPROVEMENTS:
- Added new data-source for fvCEP resource..

BUG FIXES:
- Fixed an issue with aci_physical_domain and aci_l3_domain_profile about unknown attribute error.


## 0.5.0 (October 23, 2020)

IMPROVEMENTS:
- Added new resources Spine Switch profiles and interfaces, L4-L7 interfaces.
- access_port_block have default name attribute with auto incrementor.
- Added resources to manage FEX profiles.

BUG FIXES:
- Fixed an issue with docs being not rendered via name in Hashicorp registry.
- Fixed an issue with subnet scope attribute to have list value.
- Fixed all the bugs reported.

## 0.4.1 (September 23, 2020)

IMPROVEMENTS:
- First Terraform Registry release.

## 0.4.0 (September 16, 2020)

IMPROVEMENTS:
- Improved checks in the parameters.
- Added resources to manage FEX profiles.

BUG FIXES:
- Fixed an issue with parameters not getting updated on first run.
- Fixed typo errors in documentations.

## 0.3.4 (July 20, 2020)

IMPROVEMENTS:
- Parameter `relation_cloud_rs_to_ctx` works on id now for Cloud Context Profile resource.

BREAKING CHANGES:
- Renamed all the t_dn attributes to tdn.

## 0.3.3 (July 16, 2020)

IMPROVEMENTS:
- Added zone parameter to cloud_subnet resource for APIC v5.0 or higher.

BREAKING CHANGES:
- Renamed all the e_pg attributes to epg.

## 0.3.2 (July 06, 2020)

IMPROVEMENTS:
- Updated objet model payload for l3out and vmmdomain relations.

BUG FIXES:
- Fixed the issue with vzany not updated in first run.
- FIxed the issue with switch id replaced while creating multiple switches.
## 0.3.1 (June 24, 2020)

IMPROVEMENTS:
- Updated object model for all the relation attributes compatible with new APIC versions.

## 0.3.0 (June 17, 2020)

IMPROVEMENTS:
- Added support for inline creation of filter and filter entry with contract.
- Added new resource to manage relations from epg to domain and contract with more control.
- aci_rest now supports more generic YAML/JSON payload.
- All the relation supports id only.

BUG FIXES:
- Fixed issues with domain and leaf attachment.
## 0.2.3 (May 19, 2020)

IMPROVEMENTS:
- Added new resource to manage imported_contracts.

## 0.2.2 (May 11, 2020)

BREAKING CHANGES:
- Renamed the aci_cloud_epg, aci_cloud_external_epg, aci_cloud_endpoint_selectorfor_external_epgs resources, removed an extra `_` in epg. New names for these resources will be aci_cloud_epg, aci_cloud_external_epg, aci_cloud_endpoint_selectorfor_external_epgs respectively.

IMPROVEMENTS:
- Removed the implicit status insertion for aci_rest resource.

BUG FIXES:
- Fixed the issue with l3extRsL3DomAtt not attaching properly.
## 0.2.1 (April 15, 2020)

IMPROVEMENTS:
- Added new resources for static leaf attachment, l3out profile, aci_any.
- Added support for inline private key for authentication.
## 0.2.0 (April 07, 2020)

BUG FIXES:

- Added singleton implementation for authentication endpoint.
## 0.1.8 (April 02, 2020)

IMPROVEMENTS:
- Added new modules for managing fabric and APIC management objects.
## 0.1.7 (January 27, 2020)
BUG FIXES:

- Fixed the issue with new Rn format for CloudExtEpgSelector class.
## 0.1.6 (January 25, 2020)

IMPROVEMENTS:
- Added support for new cipher suites and TLS version for the new release of cloud APIC.
## 0.1.5 (January 22, 2020)

IMPROVEMENTS:

- Added logic to handle panics and show proper error messages.
## 0.1.4 (December 20, 2019)
BUG FIXES:

- Fixed crashing of Terraform while using cert based authentication.

IMPROVEMENTS:

- Switched to terraform-plugin-sdk instead of legacy terraform package. 
## 0.1.3 (December 18, 2019)
BUG FIXES:

- Fixed issue of having 405 errors from APIC nginx.

## 0.1.2 (November 04, 2019)

BUG FIXES:

- Fixed issue of hanging sessions with Terraform 0.12.
## 0.1.1 (September 19, 2019)

IMPROVEMENTS:

- Added Docs for aci_rest resource.
- Markdown improvements.

BUG FIXES:

- Fixed issue of Terraform crashing while creating L3 Subnet.
## 0.1.0 (July 22, 2019)

- Initial Release
