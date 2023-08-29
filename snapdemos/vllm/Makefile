# installing vllm:
# 	mkvirtualenv vllm
# 	workon vllm
# 	pip install -r requirements.txt

# lists the model that is being served
listloadedmodels:
	curl -0 -v http://localhost:8000/v1/models


# serve a model with OpenAI compatible API
run-meta-opt-125m:
	python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m

# run a prediction from model being served
predict-meta-opt-125m:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "facebook/opt-125m", "prompt": "New York is ", "use_beam_search": true, "n": 4, "max_tokens": 50, "temperature": 0}'


# serve a model with OpenAI compatible API
run-meta-opt-6.7b:
	python -m vllm.entrypoints.openai.api_server --model facebook/opt-6.7b

# run a prediction from model being served
predict-meta-opt-6.7b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "facebook/opt-6.7b", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'

# serve a model with OpenAI compatible API
run-vicuna-7b:
	python -m vllm.entrypoints.openai.api_server --model lmsys/vicuna-7b-v1.3

# run a prediction from model being served
predict-vicuna-7b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "lmsys/vicuna-7b-v1.3", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'

# serve a model with OpenAI compatible API
run-falcon-7b:
	python -m vllm.entrypoints.openai.api_server --trust-remote-code --model tiiuae/falcon-7b

# run a prediction from model being served
predict-falcon-7b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "tiiuae/falcon-7b", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'

# serve a model with OpenAI compatible API
run-openllama-7b:
	python -m vllm.entrypoints.openai.api_server --model openlm-research/open_llama_7b
# torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB (GPU 0; 22.20 GiB total capacity; 21.21 GiB already allocated; 162.06 MiB free; 21.22 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
# make: *** [Makefile:22: run-openllama-13b] Error 1
# run a prediction from model being served

predict-openllama-7b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "openlm-research/open_llama_7b", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'


# serve a model with OpenAI compatible API
run-openllama-13b:
	python -m vllm.entrypoints.openai.api_server --model openlm-research/open_llama_13b
# torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB (GPU 0; 22.20 GiB total capacity; 21.21 GiB already allocated; 162.06 MiB free; 21.22 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
# make: *** [Makefile:22: run-openllama-13b] Error 1
# run a prediction from model being served

predict-openllama-13b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "openlm-research/open_llama_13b", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'

# examples that run on an A10g
ex-meta-opt:
	python3 ex-meta-opt-125m.py

ex-openai-client:
	python3 ex-openaiclient.py
