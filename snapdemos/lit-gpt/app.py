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

# from src.generate import base
from src.generate import litmodel
from pathlib import Path

# create the Flask app
app = Flask(__name__)

start = time.time()

# my_model = litmodel.LitModel(checkpoint_dir=Path("src/checkpoints/stabilityai/stablelm-base-alpha-3b"))
my_model = litmodel.LitModel(checkpoint_dir=Path("src/checkpoints/openlm-research/open_llama_7b"))

my_model.load()

end = time.time()


@app.route('/query')
def query_example():
    data = request.args.get('data')
    # output = base.main(prompt="My name is ", 
    #           checkpoint_dir=Path("src/checkpoints/stabilityai/stablelm-base-alpha-3b"))

    output = my_model.gen(prompt=data)
    # return data+" hello!\n"
    return json.dumps({"output": output})

if __name__ == '__main__':
    # run app on port 8080
    app.run(host="0.0.0.0", port=8080)
