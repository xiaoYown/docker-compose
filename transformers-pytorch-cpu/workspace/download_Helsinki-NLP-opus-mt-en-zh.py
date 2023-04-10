from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Helsinki-NLP/opus-mt-en-zh"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./cache/Helsinki-NLP/opus-mt-en-zh")
tokenizer.save_pretrained("./cache/Helsinki-NLP/opus-mt-en-zh")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)