run-falcon-7b:
	#volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run
	set -x
	docker run --gpus all --shm-size 1g -p 8080:80 -v ${HOME}/.cache/tgi/:/data ghcr.io/huggingface/text-generation-inference:1.0.2 --model-id tiiuae/falcon-7b-instruct

run_testclient:
	python3 testclient.py

run_test_curl:
	curl 127.0.0.1:8080/generate \
		-X POST \
		-d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \
		-H 'Content-Type: application/json'

run_test_curl_stream:
	curl 127.0.0.1:8080/generate_stream \
		-X POST \
		-d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \
		-H 'Content-Type: application/json'
