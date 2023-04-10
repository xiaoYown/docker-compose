# encoding: utf-8
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# 是的，Transformers 库支持多种 NLP 任务，可以通过 pipeline 方法的 task 参数来指定。以下是 Transformers 库支持的一些 NLP 任务：

# "text-generation"：文本生成，生成一段与输入文本相关的新文本。
# "translation_xx_to_yy"：翻译任务，将 xx 语言翻译为 yy 语言。
# "text-classification"：文本分类，对输入文本进行分类，例如情感分析或垃圾邮件分类。
# "token-classification"：标记分类，对输入文本中的每个标记进行分类，例如命名实体识别或词性标注。
# "question-answering"：问答任务，回答关于输入文本的问题。
# 更多任务可以查看 Transformers(https://huggingface.co/docs/transformers/main_classes/pipelines) 文档中的 “Pipelines” 一节。

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
    generator = pipeline(task, model=model_name)
    generated_text = generator(content, max_length=max_length)
    print('End')

    return jsonify({'generated_text': generated_text[0]['generated_text']})

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True)
    
