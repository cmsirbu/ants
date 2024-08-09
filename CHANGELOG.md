# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Calendar Versioning](https://calver.org/).

## [Unreleased]

## [v24.08.0]

After successful testing with the `23.11.0.lite` version of the box, the base box build via vagrant is now on a Debian 12 (bookworm) base.

### Added

- More python tooling provided out of the box as system packages `ipython, pipx, cookiecutter, invoke, networklab`.

### Changed

- ANTS is built from the `debian/bookworm64` box instead of Ubuntu.
- Python packages are not installed via the system python inside the user folder. All CLI tools are installed through `pipx` in dedicated virtual environments.
- Updated `ansible-core` to `2.17`.
- Updated `containerlab` to `0.56.0`.
- Updated `vale` to `3.7.0`.
- Updated `go` to `1.22.6`.
- Updated `poetry` to `1.8.3`.
- Updated `pyenv` to `2.4.10`.

### Removed

- All previously installed tooling via `pip` is removed.


## [v23.02.0]

This is the last major full-fat release with many Python libraries pre-installed. Due to dependency hell type issues making each release a bit of a struggle, the path onwards will be to use a leaner base with separate environments managed via `poetry` and `pyenv` to install tools as needed.

### Added

- Set up `.gitconfig` file to set the default branch to `main`.
- Symlink for `docker-compose` so it works alongside `docker compose`.
- Installed `poetry 1.3.2` and `pyenv 2.3.13`.

### Removed

- Disabled install of `pyats` and `salt-sproxy` via pip due to dependency clashes.
- Unpinned packages: `textfsm requests cryptography`.

### Changed

- Updated to Ansible 7.
- Updated base box to Ubuntu 22.04 (Jammy Jellyfish) - `ubuntu/jammy64 v20230215.0.0`.
- Tweaks to `bash.sh` aliases and prompt (which is now multiline to help with narrow terminals and nested folder paths).
    + New bash alias: `diff` for colorized unified diff`.
    + New bash alias: `ad` for `ansible-doc`.
    + New bash alias: `gls` for `gl` (pretty git log) with signatures.
- Rename `netsim-tools` to `networklab`.
- Updated `containerlab` to `0.36.1`.
- Updated `vale` to `2.23.0`.
- Updated `go` to `1.20.1`.


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
