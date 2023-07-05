build:
	cog build -t textgen-gpt2

runkontain:
	docker run --rm --runtime=krun -p 5000:5000 textgen-gpt2

rundocker:
	docker run --rm -p 5000:5000 textgen-gpt2

downloadweights:
	cog run script/download_weights

runonce:
	cog predict -i prompt="The sailor sailed into the"

predict:
	# image url is a cup
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"prompt":"The sailor sailed into the "}}' | jq '.output'
