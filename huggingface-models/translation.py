from transformers import T5ForConditionalGeneration, T5Tokenizer, FSMTForConditionalGeneration, FSMTTokenizer

import time

def runModel(model, tokenizer, input, device):
   start_time = time.time()
   
   model.to(device)
   # tokenizer = T5Tokenizer.from_pretrained(model_name)

   calc_start_time = time.time()

   # translate Russian to English
   input_ids = tokenizer(input, return_tensors="pt")
   generated_tokens = model.generate(**input_ids.to(device))
   result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

   end_time = time.time()

   calc_duration = (end_time - calc_start_time)
   total_duration = (end_time - start_time)

   print(result)
   print("calculation --- %s seconds ---" % calc_duration)
   print("total --- %s seconds ---" % total_duration)

runModel(T5ForConditionalGeneration.from_pretrained('utrobinmv/t5_translate_en_ru_zh_large_1024'), 
         T5Tokenizer.from_pretrained('utrobinmv/t5_translate_en_ru_zh_large_1024') , 'translate to en: Съешь ещё этих мягких французских булок.',
         "cuda")

runModel(FSMTForConditionalGeneration.from_pretrained("inseq/wmt21-mlqe-ru-en"), FSMTTokenizer.from_pretrained("inseq/wmt21-mlqe-ru-en"), 'Съешь ещё этих мягких французских булок.', "cuda")

