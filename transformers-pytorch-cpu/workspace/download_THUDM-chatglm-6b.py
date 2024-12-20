from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "THUDM/chatglm-6b"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

model.save_pretrained("./cache/THUDM/chatglm-6b")
tokenizer.save_pretrained("./cache/THUDM/chatglm-6b")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)