from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Answer = namedtuple('answer', 'text mood')
answers = []


@app.route('/test')
def test():
    return str(request.args.get('mood'))

@app.route('/')
@app.route('/main')
@app.route('/main/')
def main():
    return redirect(url_for('howudoing'))


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', answers=answers)


@app.route('/howudoing', methods=['GET'])
def howudoing():
    return render_template('howudoing.html')


@app.route('/howudoing/answer', methods=['GET'])
def answer():
    mood = request.args.get('mood')
    if mood is None:
        mood = 'strange'
    return render_template('answer.html', mood=mood)


@app.route('/howudoing/answer/add', methods=['POST'])
def add_answer():
    text = request.form['text']
    mood = request.form['mood']
    answers.append(Answer(text, mood))
    return redirect(url_for('home'))


app.run(host='127.0.0.1', port=5000)
