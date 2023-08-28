# # https://vllm.readthedocs.io/en/latest/models/supported_models.html
from vllm import LLM, SamplingParams

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=512)

prompts = ["Hello, my name is", "The capital of France is"]  # Sample prompts.
llm = LLM(model="lmsys/vicuna-7b-v1.3")  # Create an LLM.
outputs = llm.generate(prompts, sampling_params)  # Generate texts from the prompts.

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
