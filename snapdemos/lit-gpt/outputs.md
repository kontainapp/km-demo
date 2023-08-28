## openllama 2
python3 app.py
Loading model 'src/checkpoints/openlm-research/open_llama_7b/lit_model.pth' with {'org': 'openlm-research', 'name': 'open_llama_7b', 'block_size': 2048, 'vocab_size': 32000, 'padding_multiple': 64, 'padded_vocab_size': 32000, 'n_layer': 32, 'n_head': 32, 'n_embd': 4096, 'rotary_percentage': 1.0, 'parallel_residual': False, 'bias': False, 'n_query_groups': 32, 'shared_attention_norm': False, '_norm_class': 'RMSNorm', 'norm_eps': 1e-06, '_mlp_class': 'LLaMAMLP', 'intermediate_size': 11008, 'condense_ratio': 1}
Time to instantiate model: 0.02 seconds.
Time to load the model weights: 104.18 seconds.
model: <class 'lightning.fabric.wrappers._FabricModule'>
tokenizer: <class 'lit_gpt.tokenizer.Tokenizer'>
fabric: <class 'lightning.fabric.fabric.Fabric'>
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.31.10.140:8080
Press CTRL+C to quit
Global seed set to 1234
Home is where you live life to the fullest, and there is no better way to do that than having a home you love. We know you have a choice when you decide where you are going to live, and we would like the opportunity to help you decide
Time for inference 1: 299.75 sec total, 0.17 tokens/sec
127.0.0.1 - - [26/Aug/2023 04:32:10] "GET /query?data=Home%20is%20where HTTP/1.1" 200 -

#### ----------------------
## VM Type
AWS VM type: t2.xlarge

```bash
uname -a
Linux ip-172-31-14-35 5.19.0-1028-aws #29~22.04.1-Ubuntu SMP Tue Jun 20 19:12:11 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

free -mh
               total        used        free      shared  buff/cache   available
Mem:            15Gi       1.5Gi        13Gi       1.0Mi       822Mi        13Gi


lscpu
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         46 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  4
  On-line CPU(s) list:   0-3
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
    CPU family:          6
    Model:               79
    Thread(s) per core:  1
    Core(s) per socket:  4
    Socket(s):           1
    Stepping:            1
    BogoMIPS:            4599.99
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nop
                         l xtopology cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hyperviso
                         r lahf_lm abm cpuid_fault invpcid_single pti fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt
Virtualization features:
  Hypervisor vendor:     Xen
  Virtualization type:   full
Caches (sum of all):
  L1d:                   128 KiB (4 instances)
  L1i:                   128 KiB (4 instances)
  L2:                    1 MiB (4 instances)
  L3:                    45 MiB (1 instance)
NUMA:
  NUMA node(s):          1
  NUMA node0 CPU(s):     0-3
Vulnerabilities:
  Itlb multihit:         KVM: Mitigation: VMX unsupported
  L1tf:                  Mitigation; PTE Inversion
  Mds:                   Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown
  Meltdown:              Mitigation; PTI
  Mmio stale data:       Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown
  Retbleed:              Not affected
  Spec store bypass:     Vulnerable
  Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:            Mitigation; Retpolines, STIBP disabled, RSB filling, PBRSB-eIBRS Not affected
  Srbds:                 Not affected
  Tsx async abort:       Not affected
```



- for stable-lm-3b

```bash
make predict-stablelm-3b
cd lit-gpt && python generate/base.py --prompt "Hello, my name is Federer and I am a tennis player" --checkpoint_dir checkpoints/stabilityai/stablelm-base-alpha-3b
/home/ubuntu/.virtualenvs/litgpt/lib/python3.10/site-packages/pydantic/_migration.py:283: UserWarning: `pydantic.utils:Representation` has been removed. We are importing from `pydantic.v1.utils:Representation` instead.See the migration guide for more details: https://docs.pydantic.dev/latest/migration/
  warnings.warn(
Loading model 'checkpoints/stabilityai/stablelm-base-alpha-3b/lit_model.pth' with {'org': 'stabilityai', 'name': 'stablelm-base-alpha-3b', 'block_size': 4096, 'vocab_size': 50254, 'padding_multiple': 512, 'padded_vocab_size': 50688, 'n_layer': 16, 'n_head': 32, 'n_embd': 4096, 'rotary_percentage': 0.25, 'parallel_residual': True, 'bias': True, 'n_query_groups': 32, 'shared_attention_norm': False, '_norm_class': 'LayerNorm', 'norm_eps': 1e-05, '_mlp_class': 'GptNeoxMLP', 'intermediate_size': 16384, 'condense_ratio': 1}
Time to instantiate model: 0.07 seconds.
Time to load the model weights: 107.80 seconds.
Global seed set to 1234
Hello, my name is Federer and I am a tennis player from Germany. It's a great challenge to make tennis in french because you have to become a stronger player in each round to beat everyone. And these are the new players who come to my games. I hope to be able to play in to
Time for inference 1: 191.54 sec total, 0.26 tokens/sec


#------ 2nd Time
make predict-stablelm-3b
cd lit-gpt && python generate/base.py --prompt "Hello, my name is Federer and I am a tennis player" --checkpoint_dir checkpoints/stabilityai/stablelm-base-alpha-3b
/home/ubuntu/.virtualenvs/litgpt/lib/python3.10/site-packages/pydantic/_migration.py:283: UserWarning: `pydantic.utils:Representation` has been removed. We are importing from `pydantic.v1.utils:Representation` instead.See the migration guide for more details: https://docs.pydantic.dev/latest/migration/
  warnings.warn(
Loading model 'checkpoints/stabilityai/stablelm-base-alpha-3b/lit_model.pth' with {'org': 'stabilityai', 'name': 'stablelm-base-alpha-3b', 'block_size': 4096, 'vocab_size': 50254, 'padding_multiple': 512, 'padded_vocab_size': 50688, 'n_layer': 16, 'n_head': 32, 'n_embd': 4096, 'rotary_percentage': 0.25, 'parallel_residual': True, 'bias': True, 'n_query_groups': 32, 'shared_attention_norm': False, '_norm_class': 'LayerNorm', 'norm_eps': 1e-05, '_mlp_class': 'GptNeoxMLP', 'intermediate_size': 16384, 'condense_ratio': 1}
Time to instantiate model: 0.02 seconds.
Time to load the model weights: 114.43 seconds.
Global seed set to 1234
Hello, my name is Federer and I am a tennis player from Germany. It's a great challenge to make tennis in french because you have to become a stronger player in each round to beat everyone. And these are the new players who come to my games. I hope to be able to play in to
Time for inference 1: 191.14 sec total, 0.26 tokens/sec
```

for stable-lm-7b

```bash
make predict-stablelm-7b
cd lit-gpt && python generate/base.py --prompt "Hello, my name is Federer and I am a tennis player" --checkpoint_dir checkpoints/stabilityai/stablelm-base-alpha-7b
/home/ubuntu/.virtualenvs/litgpt/lib/python3.10/site-packages/pydantic/_migration.py:283: UserWarning: `pydantic.utils:Representation` has been removed. We are importing from `pydantic.v1.utils:Representation` instead.See the migration guide for more details: https://docs.pydantic.dev/latest/migration/
  warnings.warn(
Loading model 'checkpoints/stabilityai/stablelm-base-alpha-7b/lit_model.pth' with {'org': 'stabilityai', 'name': 'stablelm-base-alpha-7b', 'block_size': 4096, 'vocab_size': 50254, 'padding_multiple': 256, 'padded_vocab_size': 50432, 'n_layer': 16, 'n_head': 48, 'n_embd': 6144, 'rotary_percentage': 0.25, 'parallel_residual': True, 'bias': True, 'n_query_groups': 48, 'shared_attention_norm': False, '_norm_class': 'LayerNorm', 'norm_eps': 1e-05, '_mlp_class': 'GptNeoxMLP', 'intermediate_size': 24576, 'condense_ratio': 1}
Time to instantiate model: 0.02 seconds.
Killed
make: *** [Makefile:39: predict-stablelm-7b] Error 137
```