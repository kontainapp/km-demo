import argparse
import os
import sys
import re
import time
from ctypes import *

import requests
import torch
from datasets import load_dataset
from diffusers import (StableCascadeDecoderPipeline,
                       StableCascadePriorPipeline, StableCascadeUNet,
                       StableDiffusionPipeline)
from flask import Flask, jsonify, request
from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import NougatProcessor, VisionEncoderDecoderModel

app = Flask(__name__)  # define app using Flask

device = "cuda" if torch.cuda.is_available() else "cpu"

repo = "IDKiro/sdxs-512-0.9"
seed = 42
weight_type = torch.float32     # or float16

pipe = StableDiffusionPipeline.from_pretrained(
    repo, torch_dtype=weight_type).to(device)
pipe.set_progress_bar_config(disable=True)


@app.route('/make-image', methods=['POST'])
def process():
    prompt = request.values.get("prompt")

    print("promt=", prompt)
    image = pipe(
        prompt,
        num_inference_steps=1,
        guidance_scale=0,
        generator=torch.Generator(device="cuda").manual_seed(seed)
    ).images[0]

    image.save("output.png")

    return "output.png"


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
