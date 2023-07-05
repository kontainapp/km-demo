build:
	cog build -t resenet18

runkontain:
	docker run --rm --runtime=krun -p 5000:5000 resnet18

rundocker:
	docker run --rm -p 5000:5000 resnet18

runonce:
	cog predict -i @cup.jpg

predict:
	# image url is a cup
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"image":"https://dm0qx8t0i9gc9.cloudfront.net/watermarks/image/rDtN98Qoishumwih/tea-cup-drawing_z1mUGhnu_SB_PM.jpg"}}' | jq '.output'

downloadlabels:
	wget https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
