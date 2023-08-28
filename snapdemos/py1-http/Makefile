run_program:
	/opt/kontain/bin/km --mgtpipe=/tmp/mgtpipe /usr/bin/python3 -m http.server

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -I -v http://localhost:8000
