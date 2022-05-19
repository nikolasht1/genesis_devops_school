# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update -y
      echo "10.0.0.130  bento-server" >> /etc/hosts
    SHELL
    config.vm.provision :shell, path: "C:/genesis_devops_school/machineSetings.sh"
  
    config.vm.define "genesis" do |genesis|
      genesis.vm.box = "bento/ubuntu-20.04"
      genesis.vm.hostname = "bento-server"
      genesis.vm.network "private_network", ip: "10.0.0.130"
      genesis.vm.provider "virtualbox" do |vb|
      genesis.disksize.size = "30GB"
          vb.memory = 8192
          vb.cpus = 2
        end
           
    end

end
