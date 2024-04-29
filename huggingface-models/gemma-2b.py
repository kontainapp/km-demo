from transformers import AutoTokenizer, AutoModelForCausalLM
import time

# device = 'cpu'
device = 'cuda'

start_time = time.time()

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it", device_map="auto")

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt").to(device)

calc_start_time = time.time()

outputs = model.generate(**input_ids, max_new_tokens=40)

calc_duration = (time.time() - calc_start_time)
total_duration = (time.time() - start_time)
print(tokenizer.decode(outputs[0]))
print("calculation --- %s seconds ---" % calc_duration)
print("total --- %s seconds ---" % total_duration)
