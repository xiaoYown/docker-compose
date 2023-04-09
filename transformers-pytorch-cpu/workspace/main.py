# encoding: utf-8
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] = 'application/octet-stream'

@app.route('/')
def home():
    return 'Flask + Transformers Demo'

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json['content']
    model_name = request.json['model_name']
    task = request.json['task']
    max_length = request.json.get('max_length', 50)

    generator = pipeline(task, model=model_name)
    generated_text = generator(content, max_length=max_length)

    response = jsonify({'generated_text': generated_text[0]['generated_text']})
    response.headers.add('Content-Disposition', 'attachment', filename='generated_text.txt')
    return response

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)

