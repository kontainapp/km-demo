#!/bin/bash

# Copyright 2022 Kontain
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

trap "rm -f forward.conf" EXIT

[ "$TRACE" ] && set -x

URL_LIST_FILE=url-list.in
print_help() {
    echo "usage: $0  [--nginx ] [--path=url_path] [--host-name=hostname]"
    echo ""
    echo "  --nginx prepare and apply reverse proxy nginx config"
    echo "  --path  additional url path and optional parametes to add to url (defaults to /)"
    echo "  --host-name host name to use in url(defaults to localhost)"
}

do_nginx=
path="/"
host_name="localhost"

for arg in "$@"
do
   case "$arg" in
        --nginx)
            do_nginx=yes
        ;;
        --path=*)
            path="${1#*=}"
        ;;
        --host-name=*)
            host_name="${1#*=}"
    esac
    shift
done

echo "path=$path"
declare -a ip_array=($(kubectl get pod -o wide  | sort -V | awk -e '/sb-/{print $(NF - 3)}'))

total=${#ip_array[@]}

rm -f $URL_LIST_FILE

if [ -n "$do_nginx" ]; then 
    echo "configure nginx"
    rm -f forward.conf
    for (( i=1; i<=$total; i++ ))
    do
        config_str="
        location /$i {
            rewrite ^/$i(.*) /\$1 break;
            proxy_pass http://${ip_array[$(expr $i - 1)]}:8080 ;
        }
        "
        echo "$config_str" >> forward.conf
    done

    sudo cp forward.conf /etc/nginx/default.d/
    sudo systemctl restart nginx

    for (( i=1; i<=$total; i++ ))
    do
        echo "http://${host_name}/${i}/${path}" >> $URL_LIST_FILE
    done
else 
    for (( i=1; i<=$total; i++ ))
    do
        echo "http://${ip_array[$(expr $i - 1)]}:8080/${path}" >> $URL_LIST_FILE
    done
fi

