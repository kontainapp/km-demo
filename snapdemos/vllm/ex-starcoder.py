# # https://vllm.readthedocs.io/en/latest/models/supported_models.html
from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [
    "Show me a python example of opening a file",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=512)

# Create an LLM.
#llm = LLM(model="WizardLM/WizardCoder-15B-V1.0")
llm = LLM(model="bigcode/gpt_bigcode-santacoder")
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
