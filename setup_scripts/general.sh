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
sudo apt-get install -y binutils \
        curl   \
        iproute2  \
        iputils-ping \
        nano   \
        net-tools \
        unzip \ 
        arping \
        conntrack \
        curl   \
        dnsutils  \
        iptables \
        mtr-tiny  \
        netcat \
        openbsd-inetd  \
        procps \
        tcpdump   \
        telnet \
        telnetd \
        python3.8-distutils \
     && rm -rf /var/lib/apt/lists/*
     
     cd /local/repository/
     python3 /local/repository/get-pip3.py \
     pip3 install scapy
     

sudo cp bashrc /home/seed/.bashrc
chown seed: /home/seed/.bashrc
sudo cp bashrc /root/.bashrc

CMD /bin/bash
