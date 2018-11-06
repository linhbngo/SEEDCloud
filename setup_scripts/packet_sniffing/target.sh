#/bin/bash
set -x

#
# setup scapy
#
sudo /opt/anaconda3/bin/pip install scapy

#
# send infite UDP messages to instructor's machine
#
# sudo /opt/anaconda3/bin/python /local/repository/setup_scripts/packet_sniffing/udp_sender.py > /dev/null 2>&1 &
