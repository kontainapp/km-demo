#
# Copyright 2023 Kontain Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#       
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and 
# limitations under the License.
#

# import main Flask class and request object
from flask import Flask, request
from ctransformers import AutoModelForCausalLM
import sys, os
import time
import json

# create the Flask app
app = Flask(__name__)

start = time.time()
# llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')
# llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')
# llm = AutoModelForCausalLM.from_pretrained("../models/llama-2-7b.ggmlv3.q8_0.bin", model_type="llama")
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML")
end = time.time()

print(f"time to load model: {end-start}")


@app.route('/query')
def query_example():
    data = request.args.get('data')
    # output = base.main(prompt="My name is ", 
    #           checkpoint_dir=Path("src/checkpoints/stabilityai/stablelm-base-alpha-3b"))

    output = llm(data)
    # return data+" hello!\n"
    return json.dumps({"output": output})

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)
