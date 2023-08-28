import os

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # can be anything
os.environ["OPENAI_API_BASE"] = "http://localhost:8000/v1"

from langchain.llms import OpenAI

llms = OpenAI()
output = llms(
    prompt="The quick brown fox jumps",
    stop=[".", "\n"],
)

print(output)