from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "bert-base-uncased"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./cache/bert-base-uncased")
tokenizer.save_pretrained("./cache/bert-base-uncased")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)