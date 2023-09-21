import argparse
import os
from ctypes import *

from flask import (Flask, jsonify,  # import objects from the Flask model
                   request)
# from keras.models import load_model
#from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch
from transformers import pipeline, set_seed

kontain = CDLL("libkontain.so")

# import torch
app = Flask(__name__)  # define app using Flask

# print(keras.__version__)
# model = load_model('./tf_model.h5')

# NO PYTORCH
device = "cuda:0" if torch.cuda.is_available() else "cpu"
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
    kontain.snapshot("pytorch", "text-generation-gp2", 0)
    return ('', 204)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="port to run server on",
                    type=int, default=5000)
args = parser.parse_args()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=args.port)


# from transformers import GPT2Tokenizer, GPT2Model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')
# text = "Once upon a time, "
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
