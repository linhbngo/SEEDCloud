#!/bin/bash
set -x

# update Ubuntu's repository
sudo apt-get -y update

# setup Docker
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common tmux
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose
sudo apt-get install -y httping
sudo apt-get install -y jq

# the username needs to be changed
sudo usermod -aG docker seed
