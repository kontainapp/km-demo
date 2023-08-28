from flask import Flask, request
from llama_cpp import Llama
import time

# create the Flask app
app = Flask(__name__)

start=time.time()
# load gpt4
llm = Llama(model_path="../models/llama-2-7b.ggmlv3.q4_0.bin")

end=time.time()

print(f"loaded in:{end-start}")

question = "Name the planets in the Solar System"
res = llm(f"Q: {question} A: ", max_tokens=64, stop=["Q:", "\n"], echo=True)

print(f"output:{res}")
