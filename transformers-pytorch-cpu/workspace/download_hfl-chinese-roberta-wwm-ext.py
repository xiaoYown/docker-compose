from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "hfl/chinese-roberta-wwm-ext"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./cache/hfl/chinese-roberta-wwm-ext")
tokenizer.save_pretrained("./cache/hfl/chinese-roberta-wwm-ext")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)