from ctransformers import AutoModelForCausalLM
import time

start = time.time()
# Simple/Local - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')
# Intel AVX - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')
# GPU - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', gpu_layers=50)
# Simple/Download - llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML", gpu_layers=50)
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML")
end = time.time()

print(f"time to load model: {end-start}")

start = time.time()
print(llm("AI is going to"))
end = time.time()

print(f"time for inferencing: {end-start}")
