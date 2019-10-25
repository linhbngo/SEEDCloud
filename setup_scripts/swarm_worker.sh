#!/bin/bash
set -x

sleep 5m
dtoken=`cat /opt/keys/docker.swam`
echo $dtoken
sudo docker swarm join --token $dtoken 192.168.1.1:7777
