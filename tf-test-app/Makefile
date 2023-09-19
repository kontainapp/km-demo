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
#
# Build tensorflow inference app in a container and kontainer

SHELL := /bin/bash

BUILD_TF := build_tensorflow
TF := tensorflow-2.7.0-cp39-cp39-linux_x86_64.whl
MGMTPIPE := /mnt/km.sock
MGMTPIPE_HOST := tmp/km.sock

kontainer-snap: kontainer
	@rm -rf ${MGMTPIPE_HOST}
	docker run --runtime=krun -v $$(pwd)/tmp:/mnt:rw \
		--name test-app-k -d -p 5000:5000 --env=KM_MGTPIPE=${MGMTPIPE} test-app-k
	until curl --output /tmp/out.json --silent --fail -X POST -F image=@dog2.jpg 'http://localhost:5000/predict'; do sleep 0.1; done
	jq . /tmp/out.json
	sudo /opt/kontain/bin/km_cli -s ${MGMTPIPE_HOST} -t
	while [ -n "$(docker ps -f name=test-app-k -q)" ]; do sleep 1; done
	sudo chmod -R +rwx tmp
	@rm -rf ${MGMTPIPE_HOST}
	docker build -t test-app-snap-k -f Dockerfile_snap.kontain .
	docker rm -f test-app-k

kontainer: container
	docker build -t test-app-k -f Dockerfile.kontain .

container: ${BUILD_TF}/${TF}
	docker build -t test-app --build-arg TF=${TF} .

podman:
	podman pull docker-daemon:test-app-k:latest
	podman pull docker-daemon:test-app-snap-k:latest

${BUILD_TF}/${TF}:
	make -C ${BUILD_TF}
