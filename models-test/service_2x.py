import argparse
import sys
import os
import re
import time
from ctypes import *

import requests
import torch
from datasets import load_dataset
from flask import Flask, jsonify, request
from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import (DonutProcessor, NougatProcessor,
                          Pix2StructForConditionalGeneration,
                          Pix2StructProcessor, TrOCRProcessor,
                          VisionEncoderDecoderModel)

app = Flask(__name__)  # define app using Flask

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = DonutProcessor.from_pretrained(
    "naver-clova-ix/donut-base-finetuned-cord-v2")
model = VisionEncoderDecoderModel.from_pretrained(
    "naver-clova-ix/donut-base-finetuned-cord-v2").to(device)

# image only


def image_to_text_conditional(raw_image):
    # conditional image captioning
    text = "a photography of"
    inputs = processor(images=raw_image, return_tensors="pt").to(device)

    out = model.generate(**inputs)

    result = processor.decode(out[0], skip_special_tokens=True)

    return result


def image_to_text_unconditional(raw_image):
    # unconditional image captioning
    inputs = processor(raw_image, return_tensors="pt").to("cuda")
    end_time = time.time()

    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)


@app.route('/caption', methods=['POST'])
def process():
   
    uploaded_file = request.files['file']
    
    task_prompt = "<s_cord-v2>"
    decoder_input_ids = processor.tokenizer(
        task_prompt, add_special_tokens=False, return_tensors="pt").input_ids

    img = Image.open(uploaded_file.stream)
    pixel_values = processor(img,
                             return_tensors="pt").pixel_values

    outputs = model.generate(
        pixel_values.to(device),
        decoder_input_ids=decoder_input_ids.to(device),
        max_length=model.decoder.config.max_position_embeddings,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
    )

    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(
        processor.tokenizer.pad_token, "")
    # remove first task start token
    sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()
    caption = processor.token2json(sequence)

    return caption


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
