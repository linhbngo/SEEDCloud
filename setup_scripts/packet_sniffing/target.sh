#/bin/bash
set -x

#
# setup Anaconda
#
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
sudo bash -c "bash Anaconda3-5.3.0-Linux-x86_64.sh -b -p /opt/anaconda3"
sudo bash -c "echo 'ANACONDA_HOME=/opt/anaconda3/' >> /etc/profile"
sudo bash -c "echo 'PATH=/opt/anaconda3/bin:$PATH' >> /etc/profile"

#
# setup scapy
#
sudo /opt/anaconda3/bin/pip install scapy

#
# send infite UDP messages to instructor's machine
#
sudo /opt/anaconda3/bin/python /local/repository/setup_scripts/packet_sniffing/udp_sender.py > /dev/null 2>&1 &
