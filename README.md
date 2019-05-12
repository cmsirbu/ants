[![Build Status](https://travis-ci.org/cmsirbu/ants.svg?branch=master)](https://travis-ci.org/cmsirbu/ants)

# ANTS: Awesome Networking Tools Sandbox

**ANTS** is a sandbox VM (Virtual Machine) preloaded with tools and libraries useful for network programming and automation. It includes `ansible`, `python3`, `docker` and customized bash/vim plus [many networking related libraries](#wondering-whats-installed) for your enjoyment.

It primarily leverages the power of [vagrant](https://www.vagrantup.com/) to quickly start (and easily rebuild from scratch) a sandbox for you to develop and experiment without cluttering your host machine.

## Quick start - with Vagrant

1. Install the prerequisites: [vagrant](https://www.vagrantup.com/downloads.html) and [virtualbox](https://www.virtualbox.org/wiki/Downloads).
2. Right-click -> Save the [Vagrantfile](https://raw.githubusercontent.com/cmsirbu/ants/master/Vagrantfile) somewhere on your machine.
3. Run `vagrant up` in the folder where you saved the `Vagrantfile`
4. Enjoy your sandbox -> `vagrant ssh`!


## FAQ

### Wondering what's installed?

All of the packages, tools and libraries that are pre-installed can be found in [ants.yml](basebox/ants.yml).

- **python3**: `jmespath jinja2 flask docker junos-eznc netaddr paramiko netmiko pyeapi pyiosxr textfsm nxapi-plumbing ncclient napalm napalm-logs ciscoconfparse dnspython click boto3 colorama nornir tftpy pexpect pyntc pyserial pysnmp virlutils pyyaml urllib3 requests xmltodict pyang pytest`
- **ansible**: `ansible-tower-cli napalm-ansible`
- **system**: `git bash zsh vim make tree curl tcpdump tshark telnet htop openssh-client snmp nmap netcat-openbsd iputils-arping iputils-ping iputils-tracepath net-tools fping nnn`
- **containers**: `ciscotestautomation/pyats`

**Important note about Python 2.7**: the [official end of life](https://www.python.org/dev/peps/pep-0373/) date is 1st January 2020. While ANTS *still* has Python 2.7 included for backwards compatibility, all packages are pre-installed under Python 3 only.

### Why Vagrant? 

Because it allows you to easily **create, use and destroy** the same reproducible development environment anywhere.

### Can I just get a VM?

If you **just want a VM**, I'm planning to offer an `ova` file for download with each release as well or you could [build your own](#building-your-own-ants-vm).

## Building your own ANTS VM

The ANTS vagrant box is built from scratch using the scripts found in the [basebox](basebox) folder. If you clone this repository and run `vagrant up` in the `basebox` folder, a fresh Ubuntu 18.04 box will be downloaded and then the ANTS ansible playbook will be run **inside it** to install everything else (you still only need virtualbox and vagrant on your machine).

If you don't want to use `vagrant` at all, you can run the shell commands from the [basebox Vagrantfile](basebox/Vagrantfile) and the [ansible playbook](basebox/provision-ants.yml) in a VM of your choosing - just keep in mind you're on your own!

## Contributing

The main way you can help right now is by using the ANTS boxes to learn and build interesting things. If you run into trouble, point out problems with existing builds (only if you can reproduce them on a clean ants box) by [opening a new issue](https://github.com/cmsirbu/ants/issues).

To suggest a new library/package/tool, please search all issues first before opening a new one.

## Disclaimer

The ANTS virtual machine is provided **as is**. It is simply a collection of useful libraries and tools built on top of a Linux OS. The ANTS project is released under the **[MIT License](LICENSE)**, noting that all of the third-party libraries, software and OS carry their own respective licenses.

**This project, its authors and contributors provide no warranties of any kind whatsoever, and you install and use it at your own risk.**

For support or help with a particular tool or library please contact the maintainers and the community built around that project, do not open an issue under this project (unless it directly relates to how it was installed within the ANTS machine, its metadata or examples).
