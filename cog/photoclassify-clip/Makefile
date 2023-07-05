build:
	cog build -t photoclassify-clip

runkontain:
	docker run --rm --runtime=krun -p 5000:5000 photoclassify-clip

rundocker:
	docker run --rm -p 5000:5000 photoclassify-clip

runonce:
	@echo "text inputs are [photo of a cat], [photo of a dog]"
	@echo "image is that of a cat"
	@echo "output predicts likelihood of whether its photo of a cat or a dog"
	cog predict -i image="http://images.cocodataset.org/val2017/000000039769.jpg"

predict:
	@# image url is for cat instead of dog
	@echo "text inputs are [photo of a cat], [photo of a dog]"
	@echo "image is that of a cat"
	@echo "output predicts likelihood of whether its photo of a cat or a dog"
	curl -s -X POST -H 'Content-Type: application/json' http://localhost:5000/predictions   -d '{"input": {"image":"http://images.cocodataset.org/val2017/000000039769.jpg"}}' | jq .output
