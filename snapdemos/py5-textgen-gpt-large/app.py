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
from transformers import pipeline, set_seed
import time
import torch

# create the Flask app
app = Flask(__name__)

start=time.time()
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# load gpt2
generator = pipeline('text-generation', model='gpt2', device=device)
end=time.time()

print(f"loaded in:{end-start}")

@app.route('/query')
def query_example():
    data = request.args.get('data')
    set_seed(42)
    res = generator(data, max_length=30, num_return_sequences=1)
    return str(res)

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)

