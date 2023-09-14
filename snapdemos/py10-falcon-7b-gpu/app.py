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
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys, os
import time
import json
import torch

# create the Flask app
app = Flask(__name__)

start=time.time()
model = "tiiuae/falcon-7b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
end=time.time()

print(f"time to load model:{end-start}")


@app.route('/query')
def query_example():
    prompt = request.args.get('data')
    # output = base.main(prompt="My name is ", 
    #           checkpoint_dir=Path("src/checkpoints/stabilityai/stablelm-base-alpha-3b"))

    sequences = pipeline(
        prompt,
        max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )

    # for seq in sequences:
    #     print(f"Result: {seq['generated_text']}")    # return data+" hello!\n"

    return json.dumps({"output": sequences[0]['generated_text']})

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)
