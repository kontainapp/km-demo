# ref
article: https://medium.com/@mohan-gupta/running-llms-on-cpu-1455356b1b47
doc: https://llama-cpp-python.readthedocs.io/en/latest/#web-server
repo: https://github.com/abetlen/llama-cpp-python

# models binary location
https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main


## alternate ways to run

```bash
# Just to add some additional settings for others, HOST=0.0.0.0 makes it available to other clients on the same network (be aware there is no password protection), and PORT is the port, e.g.
pip install llama-cpp-python[server]
export MODEL=./models/7B HOST=0.0.0.0 PORT=2600
python3 -m llama_cpp.server

#--
# langchain
# Assuming 192.168.0.1 as the server IP, then when using original OpenAI's openai python module, you can then set openai.api_base, to use the above example:

openai.api_base = "http://192.168.0.1:2600/v1"

# and for the chatbot-ui:

docker run -e OPENAI_API_HOST=http://192.168.0.1:2600 -e OPENAI_API_KEY=dummy -p 3000:3000 ghcr.io/mckaywrigley/chatbot-ui:main

# Note: there is no trailing '/' in OPENAI_API_HOST, otherwise chatbot-ui fails to connect, also as of version 2023/05/10, OPENAI_API_KEY must contain some data, cannot be empty as I noticed too.


# other ways to run with source on github:
uvicorn --factory llama.server:app --host ${HOST} --port ${PORT}
```

# for snapshotting