from ctypes import *
from os import getenv

import torch
# from flask import Flask, jsonify, request  # import objects from the Flask model
# from keras.models import load_model
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

kontain = CDLL("libkontain.so")

# app = Flask(__name__)  # define app using Flask

# tweets = [{'content': 'dont know what todo', 'date': '17-02-2021', 'id': '1'},
#           {'content': 'doing flask and its pretty great', 'date': '18-02-2021', 'id': '2'}]

# print(keras.__version__)
# model = load_model('./tf_model.h5')

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

device = "cuda:0" # if torch.cuda.is_available() else "cpu"
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=device)

content = "The dog is very polite"
hasil = pipe(content)
print(hasil)

if getenv("MAKE_SNAPSHOT") != None:
    print(kontain.snapshot("pytorch", "sentiment", 0))

content = "The cat is rude"
hasil = pipe(content)
print(hasil)
