#!/usr/bin/env python

import geni.portal as portal
import geni.rspec.pg as RSpec
import geni.rspec.igext as IG
# Emulab specific extensions.
import geni.rspec.emulab as emulab
from lxml import etree as ET
import crypt
import random
import os.path
import sys

IMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"

disableTestbedRootKeys = True
pc = portal.Context()
request = pc.makeRequestRSpec()


pc.defineParameter("students", "Number of students",
                   portal.ParameterType.INTEGER, 1)
pc.defineParameter("password", 
                   "Password for SEED servers", 
                   portal.ParameterType.STRING, 'dees' )
params = pc.bindParameters()
pc.verifyParameters()

def Node(name):
  newnode = request.XenVM(name)
  newnode.routable_control_ip = True
  return newnode                    

# Setup experiments for individual students plus one lab instructor
lan = request.LAN()
prefixForIP = "192.168.1."
local_ip_count = 0                   
for i in range(params.students):
  if i == 0:
    node = Node("instructor")
  else:
    node = Node("student_"+str(i))
  node.cores = 2
  node.ram = 2048
  node.disk_image = IMAGE
  local_ip_count += 1                    
  iface = node.addInterface("if" + str(local_ip_count))
  iface.component_id = "eth1"
  iface.addAddress(RSpec.IPv4Address(prefixForIP + str(local_ip_count), "255.255.255.0"))
  lan.addInterface(iface)
  node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/general.sh " + params.password))

tourDescription = \
  "This profile provides a configurable SEED Lab infrastructure"
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)
  
pc.printRequestRSpec(request)
