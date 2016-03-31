Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "openstack-client"

  config.vm.synced_folder ".", "/vagrant", nfs: true

  config.vm.provision :shell, :path => "vm_provision/provision-ubuntu-14.04.sh"
  config.vm.network "private_network", ip: "10.0.0.10"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.customize ["modifyvm", :id, "--cpus", "1"]
    vb.memory = 1024
  end
end
