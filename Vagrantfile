# vi: set ft=ruby :
# https://docs.vagrantup.com

Vagrant.configure("2") do |config|

  config.vm.box = "cmsirbu/ants"

  # private management network for devices to connect to (assign .1 to host machine)
  config.vm.network 'private_network', ip: "10.250.0.11", netmask: 24

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"

    # disables console output logging to file
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end

end
