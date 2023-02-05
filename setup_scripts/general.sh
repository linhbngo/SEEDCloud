#!/bin/bash
set -x

# create a user named seed with password dees. 
useradd -m -s /bin/bash seed
echo "root:${1}" | chpasswd
echo "seed:${1}" | chpasswd

# useradd -m -p WchOyJRR.1Qrc -s /bin/bash seed
# usermod -a -G sudo seed

# activate password connection
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
service ssh restart

# update Ubuntu's repository
export DEBIAN_FRONTEND=noninteractive
apt-get -y update

# setup Docker
apt-get install -y binutils curl iproute2 iputils-ping nano
apt-get install -y net-tools unzip arping conntrack curl dnsutils 
apt-get install -y iptables mtr-tiny netcat openbsd-inetd procps
apt-get install -y tcpdump telnet telnetd python3.8-distutils
rm -rf /var/lib/apt/lists/*
     
python3 /local/repository/get-pip3.py 
pip3 install scapy

git clone https://github.com/longld/peda.git
echo "source $HOME/peda/peda.py" > $HOME/.gdbinit

cp /local/repository/bashrc.txt /home/seed/.bashrc
chown seed: /home/seed/.bashrc
cp /local/repository/bashrc.txt /root/.bashrc
