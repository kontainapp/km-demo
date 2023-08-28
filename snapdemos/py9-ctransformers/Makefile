run_test:
	/opt/kontain/bin/km /home/ubuntu/.virtualenvs/ctransformers/bin/python3 test.py

run_program:
	/opt/kontain/bin/km --mgtpipe=/tmp/mgtpipe /home/ubuntu/.virtualenvs/ctransformers/bin/python3 app.py

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -s -v http://localhost:8080/query?data=John
