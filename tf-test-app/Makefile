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

BUILD_TF := build_tensorflow
TF := tensorflow-2.7.0-cp39-cp39-linux_x86_64.whl

kontainer-snap: container
	docker run --runtime=krun -v /opt/kontain/bin/km_cli:/opt/kontain/bin/km_cli -v $(pwd)/tmp:/mnt:rw \
		--name test-app-k --rm -d -p 5000:5000 --env=KM_MGTPIPE=/tmp/km.sock test-app-k
	./test.sh
	-docker exec test-app-k /opt/kontain/bin/km_cli -s /tmp/km.sock -t
	while [ -n "$(docker ps -f name=test-app-k -q)" ]; do sleep 1; done
	chmod +rx tmp/kmsnap
	docker build -t test-app-snap-k -f Dockerfile_snap.kontain .
	podman pull docker-daemon:test-app-snap-k:latest

kontainer: container
	docker build -t test-app-k -f Dockerfile.kontain .
	podman pull docker-daemon:test-app-k:latest
	@echo "Run 'docker run --runtime=krun --name test-app-k --rm -it -p 5000:5000 test-app-k /bin/sh' to login into kontainer"

container: ${BUILD_TF}/${TF}
	docker build -t test-app --build-arg TF=${TF} .
	@echo "Run 'docker run --name test-app --rm -it -p 5000:5000 test-app /bin/sh' to login into container"

${BUILD_TF}/${TF}:
	make -C ${BUILD_TF}