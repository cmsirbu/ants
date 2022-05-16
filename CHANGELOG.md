# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Calendar Versioning](https://calver.org/).

## [Unreleased]

## [v22.05.0]

### Added

- This [CHANGELOG](/CHANGELOG.md).
- Added docker compose v2 integration.
- Added `pynetbox`, `salt-sproxy`, `ipython`, `netsim-tools`.
- Added `pynautobot` and the `networktocode.nautobot` Ansible collection.
- Added `containerlab 0.26.1`.
- Added `terraform` and `packer`, together with the Hashicorp `apt` repo.
- Added `golang 1.18.1`.
- Added `scrapli`, `scrapli-netconf`, `scrapli-cfg`, and `scrapli-community`.
- Added `vale`.

### Removed

- Removed `ntc-ansible`.
- Removed Juniper and PaloAlto roles.
- Removed bash alias overlapping with `go` command.

### Changed

- Refactored provisioning playbook.
- Updated to Ansible 5.
- Updated base box to Ubuntu 22.04 (Jammy Jellyfish) - `ubuntu/jammy64 v20220506.0.0`.
- Disabled Docker Compose install via Ansible since Vagrant provisioner takes care of that already.

## [v21.02.0] and older

Check out the respective [Release Notes](https://github.com/cmsirbu/ants/releases).
