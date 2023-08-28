# reference
article: https://lightning.ai/pages/community/community-discussions/the-ultimate-battle-of-language-models-lit-llama-vs-gpt3.5-vs-bloom-vs/


lit-gpt is a framework that runs multiple LLMs

from [lit-gpt](https://github.com/Lightning-AI/lit-gpt)

# setup
To set up environment:

```bash
mkvirtualenv litgpt
workon litgpt

# Note: Lit-GPT currently relies on flash attention from PyTorch nightly. 
#   Until PyTorch 2.1 is released you'll need to install nightly manually. 
# On CUDA
pip install --index-url https://download.pytorch.org/whl/nightly/cu118 --pre 'torch>=2.1.0dev'

# On CPU (incl Macs)
pip install --index-url https://download.pytorch.org/whl/nightly/cpu --pre 'torch>=2.1.0dev'
cd lit-gpt && pip install -r requirements.txt
```

# running LLMs
see Makefile for other models

example below of running stablelm 3b which is the smallest

```bash
make download-stablelm-3b
make convert-stablelm-3b
make predict-stablelm-3b
```
