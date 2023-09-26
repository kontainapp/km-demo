#!/bin/env python

import time

start = time.clock_gettime(time.CLOCK_REALTIME)

from os import getenv
from ctypes import *
from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("TheBloke/mpt-7B-chat-GGML", model_type="mpt", gpu_layers=100)

print("Duration: ", time.clock_gettime(time.CLOCK_REALTIME) - start)

if getenv("MAKE_SNAPSHOT") != None:
    kontain = CDLL("libkontain.so")
    print(kontain.snapshot("ctransformers", "mpt-7b-chat-GGML", 0))

prompt = "Early in the morning"
result = llm(prompt)

print(prompt, result)
