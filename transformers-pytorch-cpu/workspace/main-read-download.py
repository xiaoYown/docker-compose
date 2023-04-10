# encoding: utf-8
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask + Transformers Demo'

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json['content']
    model_name = request.json['model_name']
    task = request.json['task']
    max_length = request.json.get('max_length', 50)

    print('Start ...')
    model_path = f"./cache/{model_name}"
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    generator = pipeline(task, model=model, tokenizer=tokenizer)
    generated_text = generator(content, max_length=max_length)
    print('End')

    if generated_text:
        return jsonify({'generated_text': generated_text})
    else:
        error_message = f"Failed to generate text with model {model_name} and task {task}."
        return jsonify({'error': error_message})

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)
