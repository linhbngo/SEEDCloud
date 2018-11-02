#!/usr/bin/env python

from scapy.all import *

while True:
  msg = 'This is a UDP message'
  pkt = IP(dst='192.168.1.1')/TCP()/msg
  send(pkt)
