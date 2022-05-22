import pandas as pd
from flask import request
from flask import redirect
from flask import jsonify
from flask import Flask, render_template
from functions import validate, wordsearch, truncatelist, exclude

app = Flask(__name__,template_folder='templates')

complete = []

@app.route('/', methods=['GET','POST'])
def index():
    # from functions import validate, wordsearch, truncatelist, exclude, new_words
    if request.method == 'POST':
        validate()
        wordsearch()
        truncatelist()
        exclude(complete)
        return redirect('result.html')
    return(render_template('index.html'))

@app.route('/result.html', methods=['GET','POST'])
def result():
    return(render_template('result.html', complete = complete))

if __name__ == "__main__":
    app.run(port='8088',threaded=True)
