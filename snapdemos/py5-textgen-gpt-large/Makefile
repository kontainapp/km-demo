# install
# mkvirtualenv gpt2
# pip install -r requirements.txt

# https://huggingface.co/gpt2-large

run_program:
	/opt/kontain/bin/km --mgtpipe=/tmp/mgtpipe /home/ubuntu/.virtualenvs/gpt2/bin/python3 app.py

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -s -v http://localhost:8080/query?data=%22This%20is%20a%20good%20piece%20of%20cake%22
