from flask import Flask, render_template, request, redirect, url_for
from translators import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form.get('submit_btn') == '1':
            return redirect(url_for('text_to_morse'))
        else:
            return redirect(url_for('morse_to_text'))
    return render_template('index.html')


@app.route('/text-morse', methods=['GET', 'POST'])
def text_to_morse():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        morse = translator(prompt, 1)
        return render_template('text_to_morse.html', data=morse)
    return render_template('text_to_morse.html', data=None)


@app.route('/morse-text', methods=['GET', 'POST'])
def morse_to_text():
    if request.method == 'POST':
        morse = request.form.get('code')
        text = translator(morse, 0)
        result_dict = {
            'input': morse,
            'output': text,
            'method': 1
        }
        return render_template('morse_to_text.html', data=text)
    return render_template('morse_to_text.html', data=None)


if __name__ == '__main__':
    app.run(debug=True)
