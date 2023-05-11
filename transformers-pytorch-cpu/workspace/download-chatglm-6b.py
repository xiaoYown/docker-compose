# from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

model_name = "THUDM/chatglm-6b"

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id=model_name,
    local_dir=f"./cache/{model_name}",
    ignore_patterns=["*.bin"],
)

# import os
# from huggingface_hub import snapshot_download
# from transformers import AutoModel, AutoTokenizer

# global tokenizer, model

# model_path = f"./cache/{model_name}"

# if os.path.exists(model_path):
#     tokenizer = AutoTokenizer.from_pretrained(
#         model_name,
#         auto_load_weights=False,
#         default_data_dir=model_path,
#         verbose=1,
#         trust_remote_code=True,
#     )
#     model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
# else:
#     snapshot_download(
#         repo_id=model_name,
#         local_dir=f"./cache/{model_name}",
#         ignore_patterns=["*.bin"],
#     )
#     exit()
