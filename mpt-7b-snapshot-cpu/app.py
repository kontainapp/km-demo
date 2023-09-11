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

from flask import Flask, request
from ctransformers import AutoModelForCausalLM
import sys, os
import time
import json

# create the Flask app
app = Flask(__name__)

start = time.time()
model_id = "TheBloke/mpt-7B-chat-GGML"
llm = AutoModelForCausalLM.from_pretrained(model_id, model_type="mpt")
end = time.time()

print(f"time to load model {model_id}: {end-start}")

@app.route('/infer')
def query_example():
  prompt = request.args.get('prompt')
  print(f"received request for inference for prompt: {prompt}")
  result = llm(prompt)
  return json.dumps({"result": result})

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)
