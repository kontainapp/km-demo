from flask import Flask, jsonify, request  # import objects from the Flask model
# from keras.models import load_model
#from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch
from transformers import pipeline, set_seed

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

if __name__ == "__main__":
    app.run(host='0.0.0.0')


# from transformers import GPT2Tokenizer, GPT2Model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')
# text = "Once upon a time, "
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
