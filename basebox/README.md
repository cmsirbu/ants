# ANTS Basebox

This folder contains everything needed to build the ANTS base VM with `vagrant`.

To start the build, simply run `vagrant up` and enjoy. It will take some time (especially depending on the speed of your connection), be patient.

## Validating basic functionality

The [tests](tests) folder contains a bunch of basic tests written to ensure that libraries are not just installed, but also actually work. Some of the tests require virtual network devices (e.g. vQFX for the pyEZ tests) as defined in the [tests/inventory.yml](tests/inventory.yml) file.

To start the needed virtual network devices a helpful [Vagrantfile](../examples/lab/Vagrantfile) is provided in the examples - be warned, to boot all of them you need a fair bit of RAM!

And, finally, run the test suite:

```
# Connect to the machine
vagrant ssh
cd /vagrant/tests
make clean
make
```

## Packaging the box

Once the provisioning is done, to package the running VM as a new box, follow these steps:

```sh
vagrant ssh
# Clean up the caches and zeroize free space
sudo apt-get clean
rm -r /home/vagrant/.cache/pip
sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY
cat /dev/null > ~/.bash_history && history -c && exit

# Repackage the box from the current VM
vagrant package --output ants-basebox-1804.box

# Optionally, for local usage
# If a previous version exists, delete it
vagrant box remove ants-basebox-1804
# Add the new box to vagrant
vagrant box add ants-basebox-1804 ants-basebox-1804.box
```
