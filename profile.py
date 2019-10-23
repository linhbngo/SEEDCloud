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

IMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
IMAGE_ARM = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-ARM"

disableTestbedRootKeys = True
rspec = RSpec.Request()
pc = portal.Context()

pc.defineParameter("seedlabtype","SEED Lab",
                   portal.ParameterType.STRING,"software",
                   [("software","Software Security"),
                    ("web","Web Security"),
                    ("network","Network Security")])
pc.defineParameter("machines", "Number of physical nodes",
                   portal.ParameterType.INTEGER, 1)
params = pc.bindParameters()
pc.verifyParameters()

tourDescription = \
  "This profile provides a configurable SEED Lab infrastructure"
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
#tour.Instructions(IG.Tour.MARKDOWN,tourInstructions)
rspec.addTour(tour)

def Node(name):
  newnode = RSpec.RawPC(name)
  newnode.routable_control_ip = True
  return newnode                    

# Setup experiments for individual students plus one lab instructor
lan = RSpec.LAN()
rspec.addResource(lan)
prefixForIP = "192.168.1."
local_ip_count = 0                   
for i in range(params.machines):
  if i == 0:
    node = Node("head")
  else:
    node = Node("worker_"+str(i))
  node.disk_image = IMAGE
  local_ip_count += 1                    
  iface = node.addInterface("if" + str(local_ip_count))
  iface.component_id = "eth1"
  iface.addAddress(RSpec.IPv4Address(prefixForIP + str(local_ip_count), "255.255.255.0"))
  lan.addInterface(iface)
  node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/install_docker.sh"))
  #node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/general.sh"))
  #node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/software.sh"))
  rspec.addResource(node)   
  #if params.seedlabtype == "software":
         
pc.printRequestRSpec(rspec)
