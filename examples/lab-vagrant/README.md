# ANTS Vagrant lab

This example [Vagrantfile](Vagrantfile) allows you to spin up the following machines, each connected to the `10.250.0.0/24 vboxnet0` interface and to two internal layer2 segments:

- Juniper vQFX - Routing Engine (1GB RAM), Packet Forwarding Engine (2GB RAM)
- Arista vEOS - 2GB RAM
- Cisco Nexus9000v - 4GB RAM

### Sourcing the boxes

The vQFX boxes will be pulled automatically when you run `vagrant up` from the vagrant cloud as they are public. No such luck with Arista and Cisco, you need to login and download the `.box` files yourselves first and then add them to vagrant.

```
vagrant box add --name cisco/n9000v-703I76 nxosv-final.7.0.3.I7.6.box
vagrant box add --name arista/vEOS-lab-4.21.1.1F vEOS-lab-4.21.1.1F-virtualbox.box
```

### Booting up Nexus9000v

When running `vagrant up n9kv` for the first time you will have to wait until vagrant errors out that it can't connect, then run `vagrant provision n9kv` to configure its interfaces via `ansible`.
