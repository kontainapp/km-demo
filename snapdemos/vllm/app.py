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
import sys, os
import time
import json
from vllm import LLM, SamplingParams



# create the Flask app
app = Flask(__name__)

start = time.time()

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=512)
# Create an LLM.
#llm = LLM(model="facebook/opt-125m")
llm = LLM(model="tiiuae/falcon-7b", trust_remote_code=True)

end = time.time()
print(f"time to load model:{end-start}")

@app.route('/query')
def query_example():
    prompt = request.args.get('data')

    # it takes in an array of prompts and returns
    # an array of results of type RequestOutput
    outputs = llm.generate([prompt], sampling_params)

    generated_text = outputs[0].outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
    result = f"{prompt!r} {generated_text!r}"

    # return data+" hello!\n"
    return json.dumps({"output": result})

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)
