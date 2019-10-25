#!/bin/bash
  
sudo -H -u lngo bash -c "docker swarm init --advertise-addr 192.168.1.1:7777 --listen-addr 192.168.1.1:7777 > ~/swarm_server"
sudo -H -u lngo bash -c "more ~/swarm_server | grep 7777 | cut -d' ' -f9 | sudo tee -a /opt/keys/docker.swarm"
