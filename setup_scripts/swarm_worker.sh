#!/bin/bash
set -x

sleep 3m
dtoken=`cat /opt/keys/docker.swarm`
echo $dtoken
sudo docker swarm join --token $dtoken 192.168.1.1:7777
