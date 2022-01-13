#!/bin/bash
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
# "make all" builds it locally, takes 2 - 3 hours depending on the machine.
# "make upload" puts the result in azue file share.
# "make download" brings the result from azure share to avoid long compile

pip3 install --user pip numpy==1.21 wheel
pip3 install --user keras_preprocessing --no-deps
mkdir ${HOME}/bin
curl -s -L https://github.com/bazelbuild/bazelisk/releases/download/v1.7.5/bazelisk-linux-amd64 -o ${HOME}/bin/bazel
chmod a+x ${HOME}/bin/bazel
PATH=${PATH}:${HOME}/bin
git clone https://github.com/tensorflow/tensorflow.git -b v2.7.0
cd tensorflow
./configure < /dev/null
bazel build --jobs=$(nproc) --copt=-D_GTHREAD_USE_RECURSIVE_MUTEX_INIT_FUNC=1 //tensorflow/tools/pip_package:build_pip_package
./bazel-bin/tensorflow/tools/pip_package/build_pip_package ..
