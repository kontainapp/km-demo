#
# Copyright 2021 Kontain Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

all:
	cd JNDI-Exploit-Kit && mvn clean package -DskipTests
	make -C dialback-metasploit
	docker build log4shell-vulnerable-app/ -t vulnerable-app-kontain -f log4shell-vulnerable-app/Dockerfile.kontain
	docker build log4shell-vulnerable-app/ -t vulnerable-app

demo:
	cd JNDI-Exploit-Kit && mvn clean package -DskipTests && docker build -t log4jshell/jndi_exploit_kit .
	cd dialback-metasploit && docker rm -f msfvenom && docker build -t log4jshell/msfvenom .
	cd log4shell-vulnerable-app/ && docker build -t log4jshell/vulnerable-app . 
	cd log4shell-vulnerable-app/ && docker build -t log4jshell/vulnerable-app-kontain -f Dockerfile.kontain .
	cp msfvenom.sh /tmp/
