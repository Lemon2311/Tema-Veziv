from unsloth import FastLanguageModel
import torch
max_seq_length = 10048 # RoPE Scaling internally
dtype = None
load_in_4bit = True # 4bit quantization to reduce memory usage

# 4bit pre quantized models for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/mistral-7b-v0.3-bnb-4bit",
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    "unsloth/llama-3-8b-bnb-4bit",           # Llama-3 15 trillion tokens model 2x faster
    "unsloth/llama-3-8b-Instruct-bnb-4bit",
    "unsloth/llama-3-70b-bnb-4bit",
    "unsloth/Phi-3-mini-4k-instruct",        
    "unsloth/Phi-3-medium-4k-instruct",
    "unsloth/mistral-7b-bnb-4bit",
    "unsloth/gemma-7b-bnb-4bit",             
]

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/llama-3-8b-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

if True:
    from unsloth import FastLanguageModel
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "lora_model", # LoRA model adapter
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )
    FastLanguageModel.for_inference(model) # 2x faster inference

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

def prompt_offer(solicitarea_client):
    inputs = tokenizer(
    [
        alpaca_prompt.format(
            "Generează o ofertă detaliată pentru client bazată pe Solicitarea client, care să includă:\n■ Descrierea aplicației solicitate.\n■ Tehnologiile folosite pentru dezvoltarea aplicației (ex: stack tehnologic\n- front-end, back-end, baze de date, etc.).\n■ Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației,\ninclusiv cele care nu sunt menționate direct de client dar sunt\nnecesare (ex: secțiuni financiare, facturare, etc.).", # instruction
            solicitarea_client, # input
            "", # output - blank for generation
        )
    ], return_tensors = "pt").to("cuda")

    outputs = model.generate(**inputs, max_new_tokens = 3000, use_cache = True)
    return tokenizer.batch_decode(outputs)

import os

request_dir = "client_requests"

request_files = os.listdir(request_dir)

for request_file in request_files:
    with open(os.path.join(request_dir, request_file), "r") as file:
        solicitarea_client = file.read()

    prompt_offer_text = prompt_offer(solicitarea_client)

    # Ensure prompt_offer_text is a string
    if isinstance(prompt_offer_text, list):
        prompt_offer_text = "\n".join(prompt_offer_text)  # Join list elements with newline

    client_offer_file = os.path.join("client_offers", f"{request_file}")
    
    with open(client_offer_file, "w") as file:
        file.write(prompt_offer_text)
