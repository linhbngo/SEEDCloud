#!/bin/bash
set -x

docker service create -d -p ' + $1:8888 linhbngo/csc302:software.1204.dirtycow.0.9
