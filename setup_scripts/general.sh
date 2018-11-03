#!/bin/bash
set -x

# create a user named seed with password dees. 
sudo useradd -m -p WchOyJRR.1Qrc -s /bin/bash seed

# add seed to sudo
sudo usermod -a -G sudo seed
