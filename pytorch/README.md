# HuggingFace/Pytorch Example

This example is a HuggingFace Inference prebuilt model with an HTTP front end. It accepts a single 
statement as query encoded in the URL, and it returns whether the statement was positiive or negative
and with what certainty.

A docker container named `kontainapp/pytorch-demo-cpu:latest` is created by invoking `make`.
The container is derived from `huggingface/transformers-pytorch-cpu:latest`.

Example container start:
```
docker run --rm -p 8080:8080 kontainapp/pytorch-demo-cpu
```

Example query:
```
curl --get --data-urlencode "data=this is a good piece of cake" http://127.0.0.1:8080/query-example
```
Example output:
```
{'label': 'POSITIVE', 'score': 0.9998551607131958}
```

Probably the biggest contrivence here is the base HuggingFace pre-trained model is downloaded
into the container whenever the container is started. A smarter Dockerfile would download the model
to the container as part of the container build process. Note: until this is fixed it is going to
snapshots the appearence of an unfair advantage.

# Background

The example program, `app.py`, was built by combining to simple example programs. The first was a simple
HuggingFace inference pipeline:
```
import transformers
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
res = classifier("I've been waiting for a HuggingFace course my whole life")
print(res)
```

The second was a simple python Flask example:
```
# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    return "Query Example"

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
```
