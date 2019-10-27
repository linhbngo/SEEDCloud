#!/bin/bash
set -x
echo $1
docker service create -d -p $1:8888 --hostname $2 --host $2:$3 --network seednet dirtycow:latest
