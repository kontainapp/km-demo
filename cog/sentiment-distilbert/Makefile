build:
	cog build -t sentiment-distilbert

runkontain:
	docker run --rm --runtime=krun -p 5000:5000 sentiment-distilbert

rundocker:
	docker run --rm -p 5000:5000 sentiment-distilbert

downloadweights:
	cog run script/download_weights

runonce:
	cog predict -i content="The dog is very polite"

predict:
	# image url is a cup
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"content":"The dog is very polite"}}' | jq -r '.output'
