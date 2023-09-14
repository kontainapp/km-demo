# install with virtual environment steps:
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

PY=$$(which python3)
# KM=/opt/kontain/bin/km
KM=/home/ubuntu/km/build/opt/kontain/bin/km
# KM_CLI=/opt/kontain/bin/km_cli
KM_CLI=/home/ubuntu/km/build/opt/kontain/bin/km_cli

run_test_with_py:
	${PY} test.py

run_test:
	# /opt/kontain/bin/km ${PY} test.py
	${KM} ${PY} test.py

run_app:
	${KM} --mgtpipe=/tmp/mgtpipe  ${PY} app.py

snap:
	${KM_CLI} -s /tmp/mgtpipe

run_snap:
	${KM} ./kmsnap

run_infer:
	#curl -s -v http://localhost:8080/query?data=SpaceX
	http GET http://localhost:8080/query data=="Once upon a time"
