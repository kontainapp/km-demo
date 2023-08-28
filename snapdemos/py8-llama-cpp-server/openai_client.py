import openai

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # can be anything
openai.api_base = "http://localhost:8000/v1"

output = openai.Completion.create(
    model="text-davinci-003", # currently can be anything
    prompt="The quick brown fox jumps",
    max_tokens=5,
)

print(output)
