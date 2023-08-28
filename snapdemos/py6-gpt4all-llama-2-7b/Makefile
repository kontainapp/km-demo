# install
# mkvirtualenv gpt4all
# pip install -r requirements.txt

# https://docs.gpt4all.io/index.html

run_program:
	/opt/kontain/bin/km /home/ubuntu/.virtualenvs/gpt4all/bin/python3 app.py

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -s -v http://localhost:8080/query?data=%22The%20capital%20of%20France%20is%20%22
