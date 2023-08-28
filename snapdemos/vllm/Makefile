# installing vllm:
# 	mkvirtualenv vllm
# 	workon vllm
# 	pip install -r requirements.txt

# lists the model that is being served
listloadedmodels:
	curl -0 -v http://localhost:8000/v1/models

# serve a model with OpenAI compatible API
run-vicuna-7b:
	python -m vllm.entrypoints.openai.api_server --model lmsys/vicuna-7b-v1.3

# run a prediction from model being served
predict-vicuna-7b:
	curl -0 -v http://localhost:8000/v1/completions \
	-H "Content-Type: application/json"  \
	-d '{"model": "lmsys/vicuna-7b-v1.3", "prompt": "New York is known for ", "use_beam_search": true, "n": 4, "max_tokens": 512, "temperature": 0}'

openai-client-ex:
	python ex-openaiclient.py

ex-meta-opt:
	python ex-meta-opt-125m.py

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

# 
openai-client-ex:
	python ex-openaiclient.py

ex-meta-opt:
	python ex-meta-opt-125m.py
