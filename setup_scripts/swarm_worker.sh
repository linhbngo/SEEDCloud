#!/bin/bash

sleep 1m
sudo docker swarm join --token `sudo more /opt/keys/docker.swarm` 192.168.1.1:7777
