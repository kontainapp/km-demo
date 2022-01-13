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
# Build environment for tensorflow compile

ARG OS=ubuntu:21.04
FROM ${OS}

ARG USER=appuser
ARG UID
ARG GID
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-dev python3-pip python make git gcc g++ libc-dev curl python sudo

RUN groupadd -f -g $GID appuser && useradd -m -r -u $UID -g $GID appuser
USER appuser
