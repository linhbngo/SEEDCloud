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

disableTestbedRootKeys = True
rspec = RSpec.Request()
pc = portal.Context()

  
pc.printRequestRSpec(rspec)
