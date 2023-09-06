# install with virtual environment:
# python -m venv venv
# or (if installed)
# source venv/bin/activate
# pip install -r requirements.txt

# ref: https://github.com/marella/ctransformers
# ref: https://python.langchain.com/docs/integrations/providers/ctransformers

PY=$$(which python3)
KM=/opt/kontain/bin/km
# KM=/home/ubuntu/km/build/opt/kontain/bin/km
KM_CLI=/opt/kontain/bin/km_cli
# KM_CLI=/home/ubuntu/km/build/opt/kontain/bin/km_cli

# cd ~/km-demo/llama2-snapshot-cpu
# source venv/bin/activate

run_app_with_py:
	${PY} app.py
# /home/ubuntu/km-demo/llama2-snapshot-cpu/venv/bin/python3 app.py

run_app:
	${KM} --mgtpipe=/tmp/mgtpipe ${PY} app.py
# /home/ubuntu/km/build/opt/kontain/bin/km /home/ubuntu/km-demo/llama2-snapshot-cpu/venv/bin/python3 app.py

snap:
	${KM_CLI} -s /tmp/mgtpipe
# /home/ubuntu/km/build/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	${KM} ./kmsnap
# /home/ubuntu/km/build/opt/kontain/bin/km_cli ./kmsnap

run_infer:
	curl -s -v http://localhost:8080/infer?prompt=SpaceX
