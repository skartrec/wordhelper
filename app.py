import pandas as pd
from flask import request
from flask import redirect
from flask import jsonify
from flask import Flask, render_template
from functions import validate, wordsearch, truncatelist, new_words

app = Flask(__name__,template_folder='templates')

complete = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        validate()
        wordsearch()
        truncatelist()
        exclude = request.form['exclude']
        global excluded_words 
        excluded_words =  [ele for ele in new_words if all(ch not in ele for ch in exclude)]
        return redirect('result.html')
    return(render_template('index.html'))


@app.route('/result.html', methods=['GET','POST'])
def result():
    return(render_template('result.html', excluded_words = excluded_words))

if __name__ == "__main__":
    app.run(port='8088',threaded=True)
