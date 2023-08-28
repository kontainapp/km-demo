from ctransformers import AutoModelForCausalLM
import time

start = time.time()
# llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')
# llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')
llm = AutoModelForCausalLM.from_pretrained("../models/llama-2-7b.ggmlv3.q8_0.bin", model_type="llama")
end = time.time()

print(f"time to load model: {end-start}")

start = time.time()
print(llm("AI is going to"))
end = time.time()

print(f"time for inferencing: {end-start}")
