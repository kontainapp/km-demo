#
# Copyright 2022 Kontain Inc
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
# Build our own custom built version of tensorflow.
# The code isn't changed, we just compile it with `-D_GTHREAD_USE_RECURSIVE_MUTEX_INIT_FUNC=1`
# to disable use of non-POSIX primitives that are not supported on musl.
#
# "make BUILD=yes" builds it locally, takes 2 - 3 hours depending on the machine.
# "make upload" puts the result in azue file share.
# "make" brings the result from azure share to avoid long compile

OS := ubuntu:21.04
TF := tensorflow-2.7.0-cp39-cp39-linux_x86_64.whl
TOP := $(shell git rev-parse --show-toplevel)
UID := $(shell id -u)
GID := $(shell id -g)

all: ${TF}

${TF}:
ifeq (${BUILD},yes)
	docker build -t buildenv_tf --build-arg UID=${UID} --build-arg GID=${GID} --build-arg OS=${OS} .
	docker run --rm --name build_tf -v ${TOP}:${TOP}:z -w $(shell pwd) -u ${UID}:${GID} buildenv_tf ./build_tf.sh
else
	az storage file download --only-show-errors --no-progress --output none --share tensorflow --account-name ktf --path ${TF}
endif

upload: ${TF}
	az storage file upload --only-show-errors --share tensorflow --account-name ktf --source ${TF}
