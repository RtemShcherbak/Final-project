from flask import Flask, render_template, request, make_response, jsonify
from model import generate_answer


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def testing():
    return make_response(jsonify({'Test': 'OK'}), 200)

@app.route('/model', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']
        
        sample_data = {'context': context, 'question': question}
        answer = generate_answer(sample_data)
        return render_template('index.html', 
                               context = context,
                               question = question,
                               answer = answer)
    else:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


 