build:
	cog build -t object-detection-yolo-tiny

runkontain:
	docker run --rm --runtime=krun -p 5000:5000 object-detection-yolo-tiny

rundocker:
	docker run --rm -p 5000:5000 object-detection-yolo-tiny

downloadweights:
	cog run script/download_weights

runonce:
	cog predict -i image_url="http://images.cocodataset.org/val2017/000000039769.jpg"

predict:
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"image_url":"http://images.cocodataset.org/val2017/000000039769.jpg"}}' | jq -r '.output'
