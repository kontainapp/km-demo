# install with virtual environment:
# mkvirtualenv ctransformers
# or (if installed)
# workon ctransformers

# ref: https://github.com/marella/ctransformers
# ref: https://python.langchain.com/docs/integrations/providers/ctransformers

# pip install -r requirements.txt
PY=$$(which python3)
# KM=/opt/kontain/bin/km
KM=/home/ubuntu/km/build/opt/kontain/bin/km
# KM_CLI=/opt/kontain/bin/km_cli
KM_CLI=/home/ubuntu/km/build/opt/kontain/bin/km_cli

run_test1_with_py:
	# drop-cache: echo 3 | sudo tee /proc/sys/vm/drop_caches
	${PY} test1.py

run_test2_with_py:
	# drop-cache: echo 3 | sudo tee /proc/sys/vm/drop_caches
	${PY} test2.py

run_test:
	# /opt/kontain/bin/km ${PY} test1.py
	${KM} ${PY} test.py

run_test2:
	# /opt/kontain/bin/km ${PY} test2.py
	${KM} ${PY} test2.py

run_program:
	${KM} --mgtpipe=/tmp/mgtpipe ${PY} app.py

snap:
	${KM_CLI} -s /tmp/mgtpipe

run_snap:
	${KM} ./kmsnap

response:
	curl -s -v http://localhost:8080/query?data=John
