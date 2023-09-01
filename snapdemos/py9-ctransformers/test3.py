from ctransformers import AutoModelForCausalLM
import time

# load kontain library
kontain = CDLL("libkontain.so")

start = time.time()
# Simple/Local - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2')
# Intel AVX - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', model_type='gpt2', lib='avx')
# GPU - llm = CTransformers(model='/path/to/ggml-gpt-2.bin', gpu_layers=50)
# Simple/Download - llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML", gpu_layers=50)
# llm = AutoModelForCausalLM.from_pretrained("../models/llama-2-7b.ggmlv3.q8_0.bin", model_type="llama")
# llm = AutoModelForCausalLM.from_pretrained("../models/llama-13b.ggmlv3.q8_0.bin", model_type="llama")
model_id = "TheBloke/Llama-2-7B-GGML"
print(f"loading model {model_id}")
llm = AutoModelForCausalLM.from_pretrained(model_id)
end = time.time()

print(f"time to load model: {end-start}")

# make snapshot
if getenv("MAKE_SNAPSHOT") != None:
    print(kontain.snapshot("pytorch", "sentiment", 0))

start = time.time()
print(llm("AI is going to"))
end = time.time()

print(f"time for inferencing: {end-start}")
