import argparse
import os
import sys
from ctypes import *

# from keras.models import load_model
# from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch
from flask import Flask, jsonify, request
from transformers import pipeline, set_seed

# import torch
app = Flask(__name__)  # define app using Flask

# print(keras.__version__)
# model = load_model('./tf_model.h5')

# NO PYTORCH
device = "cuda:0" if torch.cuda.is_available() else "cpu"

print("using device ", device)

generator = pipeline('text-generation', model='gpt2', device=device)


@app.route('/predict', methods=['GET'])
def predict():
    content = request.json['content']
    set_seed(42)
    output = generator(content, max_length=30, num_return_sequences=1)
    print(output)

    return jsonify({'input': content, 'generated_text': output})


@app.route('/', methods=['GET'])
def index():
    return ""


@app.get('/shutdown')
def shutdown():
    os.kill(os.getpid(), 2)
    return ('', 204)


@app.get('/snapshot')
def snapshot():
    try:
        kontain = CDLL("libkontain.so")
        kontain.snapshot("pytorch", "text-generation-gp2", 0)
        return ('', 204)
    except Exception as e:
        print("The error is: ", e)
        return ('', 501)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="port to run server on",
                    type=int, default=5000)
parser.add_argument("-l", "--load", help="pre-load model",
                    action="store_true")

args = parser.parse_args()

if __name__ == "__main__":
    if args.load:
        print("load completed. Exiting")
        sys.exit(0)

    app.run(host='0.0.0.0', port=args.port)


# from transformers import GPT2Tokenizer, GPT2Model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')
# text = "Once upon a time, "
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
