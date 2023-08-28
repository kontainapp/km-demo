# description
This folder reproduces several ways to run some of the popular Opensource LLMs.

The usual huggingface method doesn't support these big LLMs so several projects have come up
to run them in a few different ways.

# steps to reproduce
## Example 1: using CTransformers to run llama2 GGML model

```bash
# download the llama2 models first
cd models
make download-llama2-7b


# run example
cd py9-ctransformers

# 1 time step - install virtual environment
mkvirtualenv ctransformers
pip install -r requirements.txt

# if virtual environment is installed, virtual environment
workon ctransformers

# to see it working
make run_test_with_py

# to reproduce it with error in km
make run_test
```

## Example 2: using llama cpp to run llama2 GGML model
```bash
cd py7-llama-cpp-qna

# 1-time step: install virtual environment
mkvirtualenv llamacpp
pip install -r requirements.txt

# if virtual environment is installed, virtual environment
workon llamacpp

# to see it working
make run_test_with_py

# to reproduce error in km
make run_test
```

## Example 3: using gpt4all (another popular way to load local llms)
```bash
cd py6-gpt4all-llama-2-7b

# 1-time step: install virtual environment
mkvirtualenv gpt4all
pip install -r requirements.txt

# if virtual environment is installed, virtual environment
workon gpt4all

# run this server in plain python
make run_program_with_py

# get response using curl
make response
# you will see an output

# to reproduce error in km
make run_program

# NOTE: you will notice an error in dns resolution of gpt4all.io
```

## Example 4: using lit-gpt (use pytorch lightning to run various LLM models)
```bash
# setup models
make download-stablelm-3b
make convert-stablelm-3b

# to see it working with plain python
make run_test_with_py

# to reproduce error with km
make run_test
```