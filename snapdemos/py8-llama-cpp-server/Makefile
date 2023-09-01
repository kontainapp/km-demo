# install
# mkvirtualenv llamacpp
# pip install -r requirements.txt
# for qna llamacpp: https://llama-cpp-python.readthedocs.io/en/latest/
# for generation: https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.llama.Llama.generate
# for ggml-model.bin - https://huggingface.co/Pi3141/alpaca-native-7B-ggml/tree/main

export MODEL=../models/llama-2-7b.ggmlv3.q4_0.bin
export HOST="0.0.0.0"
# export KM_MGTDIR=/tmp

run_program_with_py:
	# python3 -m llama_cpp.server
	python3 app.py

run_program:
	/opt/kontain/bin/km /home/ubuntu/.virtualenvs/llamacpp/bin/python3 -m llama_cpp.server

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -s -XPOST \
	-H "Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
	-H "Content-Type: application/json" \
	http://localhost:8000/v1/completions \
	-d '{"model": "text-davinci-003", "prompt": "The quick brown fox jumps", "max_tokens": 5}' \
	 | jq '.choices[]'.text
