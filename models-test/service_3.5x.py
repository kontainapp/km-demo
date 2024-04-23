import argparse
import os
import sys
import re
import time
from ctypes import *

import requests
import torch
from datasets import load_dataset
from flask import Flask, jsonify, request
from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import (AutoTokenizer, VisionEncoderDecoderModel,
                          ViTImageProcessor)

app = Flask(__name__)  # define app using Flask

device = "cuda" if torch.cuda.is_available() else "cpu"

model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning").to(device)
feature_extractor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning")


@app.route('/caption', methods=['POST'])
def process():
    images = []
    uploaded_file = request.files['file']
    img = Image.open(uploaded_file.stream).convert(mode="RGB")
    images.append(img)

    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    pixel_values = feature_extractor(
        images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds


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
