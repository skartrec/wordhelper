import pandas as pd
from flask import request
from flask import redirect
from flask import jsonify
from flask import Flask, render_template
from functions import new_words

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/', methods=['GET','POST'])
def search():
    from functions import validate, wordsearch, truncatelist
    if request.method == 'POST':
        form = request.form
        validate()
        wordsearch()
        truncatelist()
        return redirect('result.html')
    return(render_template('index.html'))

@app.route('/result.html', methods=['GET','POST'])
def result():
    return(render_template('result.html', new_words = new_words))
    

if __name__ == "__main__":
    app.run(port='8088',threaded=True)