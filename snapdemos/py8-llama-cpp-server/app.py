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
from llama_cpp import Llama
import time

# create the Flask app
app = Flask(__name__)

start=time.time()
# load gpt4
llm = Llama(model_path="../models/llama-2-7b-chat.ggmlv3.q4_0.bin")

end=time.time()

print(f"loaded in:{end-start}")

@app.route('/query')
def query_example():
    question = request.args.get('data')
    res = llm(f"Q: {question} A: ", max_tokens=64, stop=["Q:", "\n"], echo=True)
    return str(res)

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)

