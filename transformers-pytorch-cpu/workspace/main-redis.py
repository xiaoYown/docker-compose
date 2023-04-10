# encoding: utf-8
import redis
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
cache = redis.Redis(host='192.168.50.97', port=6379, db=0)

@app.route('/')
def home():
    return 'Flask + Transformers Demo'

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json['content']
    model_name = request.json['model_name']
    task = request.json['task']
    max_length = request.json.get('max_length', 50)

    cache_key = f'{model_name}-{task}-{content}-{max_length}'
    generated_text = cache.get(cache_key)

    if generated_text is not None:
        return jsonify({'generated_text': generated_text.decode('utf-8')})
    else:
        generator = pipeline(task, model=model_name)
        generated_text = generator(content, max_length=max_length)[0]['generated_text']
        cache.set(cache_key, generated_text.encode('utf-8'), ex=60)
        return jsonify({'generated_text': generated_text})
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)
    