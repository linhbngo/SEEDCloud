#!/bin/bash
set -x

# create a user named seed with password dees. 
sudo useradd -m -p WchOyJRR.1Qrc -s /bin/bash seed
sudo usermod -a -G sudo seed

# activate password connection
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo service ssh restart

# update Ubuntu's repository
sudo apt-get -y update

# setup Docker
sudo apt-get install -y tmux

