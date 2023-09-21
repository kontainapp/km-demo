import argparse
import os
from ctypes import *

import torch
from flask import Flask, jsonify, request
# from keras.models import load_model
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          TextClassificationPipeline)

# import torch
app = Flask(__name__)  # define app using Flask

# tweets = [{'content': 'dont know what todo', 'date': '17-02-2021', 'id': '1'},
#           {'content': 'doing flask and its pretty great', 'date': '18-02-2021', 'id': '2'}]

# print(keras.__version__)
# model = load_model('./tf_model.h5')

tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

device = "cuda:0" if torch.cuda.is_available() else "cpu"


pipe = TextClassificationPipeline(
    model=model, tokenizer=tokenizer, device=device)


@app.route('/predict', methods=['GET'])
def predict():
    content = request.json['content']

    hasil = pipe(content)
    print(hasil[0]['label'])
    return jsonify({'message': content, 'sentiment': hasil[0]['label']})


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
        kontain.snapshot("pytorch", "sentiment", 0)
        return ('', 204)
    except Exception as e:
        print("The error is: ", e)
        return ('', 501)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="port to run server on",
                    type=int, default=5000)
args = parser.parse_args()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=args.port)
