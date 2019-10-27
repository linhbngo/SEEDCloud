#!/bin/bash
set -x
echo $1
docker service create -d -p ' + $1:8888 linhbngo/csc302:software.1204.dirtycow.0.9
