# vi: set ft=ruby :
# https://docs.vagrantup.com

Vagrant.configure("2") do |config|
  # https://github.com/cmsirbu/ants
  config.vm.box = "cmsirbu/ants"

  # private management network for devices to connect to (assign .1 to host machine)
  # config.vm.network 'private_network', ip: "10.250.0.11", netmask: 24

  # 1024 is default, modify as needed
  # config.vm.provider "virtualbox" do |vb|
  #   vb.memory = "1024"
  # end

  # example provisioner for adding more packages
  # config.vm.provision "shell", privileged: false, inline: <<-SHELL
  #   pip3 install -U --user -r /vagrant/requirements.txt
  # SHELL
end
