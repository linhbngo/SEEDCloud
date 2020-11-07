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

def Node(name):
  newnode = RSpec.RawPC(name)
  newnode.routable_control_ip = True
  return newnode                    

node = Node("head")
node.disk_image = IMAGE
rspec.addResource(node)   
  
tourDescription = \
  "This profile provides a single node for SEED Lab infrastructure"
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
rspec.addTour(tour)
  
pc.printRequestRSpec(rspec)
