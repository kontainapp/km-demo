test:
	python image_from_text.py --text='artificial intelligence' --no-mega

build:
	cog build -t imagegen-min-dalle

runkontain:
	docker run -v `pwd`:/src --rm --runtime=krun -p 5000:5000 imagegen-min-dalle

rundocker:
	docker run -v `pwd`:/src --rm -p 5000:5000 imagegen-min-dalle

downloadweights:
	cog run script/download_weights

runonce:
	cog predict -i prompt="white dog on beach"

predict:
	# image url is a cup
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"prompt":"white cat on beach"}}'|jq .output
