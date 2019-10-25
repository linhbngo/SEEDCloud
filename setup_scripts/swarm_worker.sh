#!/bin/bash

sleep 1m
docker swarm join --token `more /opt/keys/docker.swarm` 192.168.1.1:7777
