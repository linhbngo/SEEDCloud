#!/bin/bash
set -x
echo $1
docker service create -d -p $1:8888 --hostname $2 --host $2:$3 --network seednet linhbngo/csc302:software.1204.dirtycow.0.9
