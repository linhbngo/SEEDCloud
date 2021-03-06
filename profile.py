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
pc.defineParameter("students", "Number of students",
                   portal.ParameterType.INTEGER, 1)
params = pc.bindParameters()
pc.verifyParameters()

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
    node = Node("worker_"+str(i + 1))
  node.disk_image = IMAGE
  local_ip_count += 1                    
  iface = node.addInterface("if" + str(local_ip_count))
  iface.component_id = "eth1"
  iface.addAddress(RSpec.IPv4Address(prefixForIP + str(local_ip_count), "255.255.255.0"))
  lan.addInterface(iface)
  
  # setup NFS
  if i == 0:
    node.addService(RSpec.Execute("sh", "sudo apt-get update"))
    node.addService(RSpec.Execute("sh", "sudo apt-get install -y nfs-kernel-server"))
    node.addService(RSpec.Execute("sh", "sudo mkdir -p /opt/keys"))
    node.addService(RSpec.Execute("sh", "sudo chown nobody:nogroup /opt/keys"))
    for k in range(1,params.machines):
      node.addService(RSpec.Execute("sh", "sudo echo '/opt/keys 192.168.1." + str(k+1) + "(rw,sync,no_root_squash,no_subtree_check)' | sudo tee -a /etc/exports"))
    node.addService(RSpec.Execute("sh", "sudo systemctl restart nfs-kernel-server"))
  else:
    node.addService(RSpec.Execute("sh", "sudo apt-get update"))
    node.addService(RSpec.Execute("sh", "sudo apt-get install -y nfs-common"))
    node.addService(RSpec.Execute("sh", "sudo mkdir -p /opt/keys"))
    node.addService(RSpec.Execute("sh", "sleep 3m"))
    node.addService(RSpec.Execute("sh", "sudo mount 192.168.1.1:/opt/keys /opt/keys"))
  
  # setup Docker and Kubernetes 
  node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/install_docker.sh"))
  node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/install_kubernetes.sh"))

  # launch swarm
  if i == 0:
    node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/swarm_manager.sh"))
    node.addService(RSpec.Execute("sh", "sleep 4m"))    
  else: 
    node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/swarm_worker.sh"))
    
  """
  # deploy lab containers
  if params.seedlabtype == "software":
    if i == 0:
      node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/build_dirtycow.sh"))
      for k in range(params.students):
        tmpPort = str(8800 + k + 1)
        tmpHost = ' seat' + str(k + 1) + ' '
        tmpIP = '10.0.0.' + str(k + 1)
        node.addService(RSpec.Execute("sh", "sudo bash /local/repository/setup_scripts/launch_dirtycow.sh " + tmpPort + tmpHost + tmpIP))
  """
  rspec.addResource(node)   
  

tourDescription = \
  "This profile provides a configurable SEED Lab infrastructure"
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
tourInstruction = ''
for i in range(params.students):
  tmpPort = str(8800 + i + 1)
  tourInstruction += '[Seat ' + str(i + 1) + '](http://{host-head}:' + tmpPort + '/)\n'

tour.Instructions( IG.Tour.MARKDOWN, tourInstruction)
rspec.addTour(tour)
  
pc.printRequestRSpec(rspec)
