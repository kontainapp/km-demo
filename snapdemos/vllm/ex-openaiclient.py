import openai
# Modify OpenAI's API key and API base to use vLLM's API server.
openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"
completion = openai.Completion.create(model="lmsys/vicuna-7b-v1.3",
                                      prompt="San Francisco is a",
                                      max_tokens=512)
print("Completion result:", completion)