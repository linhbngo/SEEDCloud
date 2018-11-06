#!/bin/bash
set -x

#
# update Ubuntu's repository
#
sudo apt-get -y update

#
# setup nmap
#
sudo apt-get -y install nmap

#
# open port 9090 and 9999 for all communications
#
sudo ufw allow 9090
sudo ufw allow 9999

#
# setup Anaconda
#
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
sudo bash -c "bash Anaconda3-5.3.0-Linux-x86_64.sh -b -p /opt/anaconda3"
sudo bash -c "echo 'ANACONDA_HOME=/opt/anaconda3/' >> /etc/profile"
sudo bash -c "echo 'PATH=/opt/anaconda3/bin:$PATH' >> /etc/profile"

# create a user named seed with password dees. 
sudo useradd -m -p WchOyJRR.1Qrc -s /bin/bash seed

# add seed to sudo
sudo usermod -a -G sudo seed
