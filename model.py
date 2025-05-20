from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model():
    model_name = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    return model, tokenizer

def filter_strings_with_model(strings_list, model, tokenizer):
    strings_blob = "\n".join(strings_list)
    prompt = f"""You are a reverse engineer. Given raw strings from a binary file, extract only interesting parts:
- Credentials, secrets, API keys
- Commands, hardcoded flags
- Suspicious IPs or URLs
- Malware-specific keywords

Ignore debug text like "process failed" or usage messages.

STRINGS:
{strings_blob}
"""

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    output = model.generate(input_ids, max_new_tokens=1024, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True)
