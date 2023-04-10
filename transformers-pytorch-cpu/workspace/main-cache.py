# encoding: utf-8
import os
import json
import hashlib
import torch
from transformers import pipeline, AutoTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# set cache path
CACHE_DIR = "./cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

@app.route('/')
def home():
    return 'Flask + Transformers Demo'

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json['content']
    model_name = request.json['model_name']
    task = request.json['task']
    max_length = request.json.get('max_length', 50)

    # create cache key from input parameters
    cache_key = hashlib.sha256(json.dumps((model_name, task, content, max_length)).encode('utf-8')).hexdigest()
    cache_file = os.path.join(CACHE_DIR, f"{cache_key}.pt")

    # check if the cache exists
    if os.path.exists(cache_file):
        model = torch.load(cache_file)
    else:
        # load the model and save it to the cache
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = pipeline(task, model=model_name)
        torch.save(model, cache_file)

    # generate the text using the model
    generated_text = model(content, max_length=max_length)[0]['generated_text']
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)