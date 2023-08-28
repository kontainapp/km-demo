# install
# mkvirtualenv llamacpp
# pip install -r requirements.txt
# for qna llamacpp: https://llama-cpp-python.readthedocs.io/en/latest/
# for generation: https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.llama.Llama.generate

run_test_with_py:
	python3 test.py

run_test:
	/opt/kontain/bin/km /home/ubuntu/.virtualenvs/llamacpp/bin/python3 test.py

run_program:
	/opt/kontain/bin/km /home/ubuntu/.virtualenvs/llamacpp/bin/python3 app.py

snap:
	/opt/kontain/bin/km_cli -s /tmp/mgtpipe

run_snap:
	/opt/kontain/bin/km ./kmsnap

response:
	curl -s -v http://localhost:8080/query?data=%22Q.%20Name%20the%20planets%20in%20solar%20system?%20A:%20%22
	# Name the planets in the solar system?

# {'id': 'cmpl-4a888aae-faca-46cd-8771-fe9a6ed4fa60', 'object': 'text_completion', 'created': 1692916452, 'model': 'models/llama-2-7b.ggmlv3.q4_0.bin', 'choices': [{'text': 'Q: "Q. Name the planets in solar system? %A: " A: 1) Mercury,2) Venus,3) Earth,4) Mars,5) Jupiter,6) Saturn,7) Uranus,8) Neptune and9) Pluto. ', 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 21, 'completion_tokens': 47, 'total_tokens': 68}}# Name the planets in the solar system?
