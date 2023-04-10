from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "hfl/chinese-electra-180g-small-discriminator"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./cache/hfl/chinese-electra-180g-small-discriminator")
tokenizer.save_pretrained("./cache/hfl/chinese-electra-180g-small-discriminator")

# Usage
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "path/to/saved_model"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)