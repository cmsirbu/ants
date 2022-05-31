[![Build Status](https://travis-ci.org/cmsirbu/ants.svg?branch=master)](https://travis-ci.org/cmsirbu/ants)

# ANTS: Awesome Networking Tools Sandbox

**ANTS** is a sandbox VM (Virtual Machine) preloaded with tools and libraries useful for network programming and automation. It includes `ansible`, `python3`, and `docker`, with customized bash/vim configurations, plus [many networking related libraries](#wondering-whats-installed) for your enjoyment.

It primarily leverages the power of [vagrant](https://www.vagrantup.com/) to quickly start (and easily rebuild from scratch) a sandbox for you to develop and experiment without cluttering your host machine.

## Quick start - with Vagrant

1. Install the prerequisites: [vagrant](https://www.vagrantup.com/downloads.html) and [virtualbox](https://www.virtualbox.org/wiki/Downloads).
2. Right-click -> Save the [Vagrantfile](https://raw.githubusercontent.com/cmsirbu/ants/master/Vagrantfile) somewhere on your machine.
3. Run `vagrant up` in the folder where you saved the `Vagrantfile`
4. Enjoy your sandbox -> `vagrant ssh`!


## FAQ

### Wondering what's installed?

All of the packages, tools and libraries that are pre-installed can be found in [ants.yml](basebox/ants.yml).

- **python3**: `python3-dev jmespath jinja2 flask docker junos-eznc netaddr paramiko netmiko pyeapi textfsm ntc-templates nxapi-plumbing ncclient napalm napalm-logs ciscoconfparse dnspython click psutil boto3 colorama nornir tftpy pexpect pyats pyntc pyserial pysnmp virlutils pyyaml urllib3 requests xmltodict pyang pytest cryptography tox pylama pan-python pynxos jxmlease yangson yangify rich invoke pynetbox pynautobot netutils ipython salt-sproxy netsim-tools scrapli scrapli_netconf scrapli-cfg scrapli-community`
- **ansible**: `ansible-tower-cli ansible-lint networktocode.nautobot napalm.napalm`
- **system**: `git bash zsh vim make tree curl tcpdump sshpass tshark telnet htop openssh-client snmp nmap netcat-openbsd iputils-arping iputils-ping iputils-tracepath net-tools fping nnn build-essential libxml2-dev libxml2-utils libxslt1-dev libffi-dev libssl-dev`
- **containers**: `docker-ce docker-compose`

### Why Vagrant?

Because it allows you to easily **create, use and destroy** the same reproducible development environment anywhere.

### Can I just get a VM image?

Older releases had an export of the Vagrant VM, but it wasn't really that useful. With the planned migration to packer, I expect to have a properly built `ova` for each release again.

## Building your own ANTS VM

The ANTS vagrant box is built from scratch using the scripts found in the [basebox](basebox) folder. If you clone this repository and run `vagrant up` in the `basebox` folder, a fresh Ubuntu box will be downloaded and then the ANTS ansible playbook will be run **inside it** to install everything else (you still only need virtualbox and vagrant on your machine).

If you don't want to use `vagrant` at all, you can run the shell commands from the [basebox Vagrantfile](basebox/Vagrantfile) and the [ansible playbook](basebox/provision-ants.yml) in a VM of your choosing - just keep in mind you're on your own!

## Contributing

The main way you can help right now is by using the ANTS boxes to learn and build interesting things. If you run into trouble, point out problems with existing builds (only if you can reproduce them on a clean ants box) by [opening a new issue](https://github.com/cmsirbu/ants/issues).

To suggest a new library/package/tool, please search all issues first before opening a new one.

## Disclaimer

The ANTS virtual machine is provided **as is**. It is simply a collection of useful libraries and tools built on top of a Linux OS. The ANTS project is released under the **[MIT License](LICENSE)**, noting that all of the third-party libraries, software and OS carry their own respective licenses.

**This project, its authors and contributors provide no warranties of any kind whatsoever, and you install and use it at your own risk.**

For support or help with a particular tool or library please contact the maintainers and the community built around that project, do not open an issue under this project (unless it directly relates to how it was installed within the ANTS machine, its metadata or examples).
