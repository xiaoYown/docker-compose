from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./cache/distilgpt2")
tokenizer.save_pretrained("./cache/distilgpt2")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)