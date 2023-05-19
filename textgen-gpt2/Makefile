#
# Copyright 2023 Kontain Inc
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

DEMO_IMAGE ?= kontainapp/sentiment-demo
SNAP_IMAGE ?= kontainapp/sentiment-demo-snap
DEMO_CONTAINER ?= kontainapp_sentiment_deo

INTERIM_IMAGE := tmp:$(shell echo $$BASHPID)
MGTDIR := /mnt
MGTDIR_HOST := tmp

MGMTPIPE_HOST := tmp/kmpipe.python3*.1
MGMTSNAP_HOST := tmp/kmsnap.python3*.1

all: build-snap

build-demo: huggingface/hub
	docker build -t ${DEMO_IMAGE} -f Dockerfile .

huggingface/hub:
	mkdir -p huggingface
	docker build -t ${INTERIM_IMAGE} -f Dockerfile .
	docker run -d --rm --name ${DEMO_CONTAINER} -p 5000:5000 ${INTERIM_IMAGE}
	curl --retry-all-errors --retry 300 --retry-delay 1 -XGET -H "Content-Type: application/json" -H "Accept: application/json" http://localhost:5000/predict -d '{"content":"The dog is very polite"}'
	docker cp ${DEMO_CONTAINER}:/root/.cache/huggingface .
	docker rm -f ${DEMO_CONTAINER}
	docker rmi ${INTERIM_IMAGE}

build-snap: build-demo
	@rm -rf ${MGMTPIPE_HOST}; mkdir -p tmp; sudo chmod a+rwx tmp
	docker run --runtime=krun -v $$(pwd)/tmp:/mnt:rw \
		--name ${DEMO_CONTAINER} -d -p 5000:5000 --env=KM_MGTDIR=${MGTDIR} ${DEMO_IMAGE}
	curl --retry-all-errors --retry 30 --retry-delay 1 --get --data-urlencode "data=this is a good piece of cake" http://127.0.0.1:5000/query
	sleep 1
	sudo /opt/kontain/bin/km_cli -s ${MGMTPIPE_HOST} -t
	while [ -n "$(docker ps -f name=${DEMO_CONTAINER} -q)" ]; do sleep 0.1; done
	rm -f ${MGMTPIPE_HOST} ${MGTDIR_HOST}/kmsnap.*.conf
	sudo chmod +rx $(shell echo ${MGMTSNAP_HOST})
	docker export ${DEMO_CONTAINER} | docker import - ${INTERIM_IMAGE}
	docker build -t ${SNAP_IMAGE} --build-arg BASE_IMAGE=${INTERIM_IMAGE} --build-arg TARGET_SNAP=$(shell echo ${MGMTSNAP_HOST}) -f Dockerfile.snap .
	docker rm -f ${DEMO_CONTAINER}
	docker rmi -f ${INTERIM_IMAGE}

podman:	
	podman pull docker-daemon:${DEMO_IMAGE}:latest
	podman pull docker-daemon:${SNAP_IMAGE}:latest