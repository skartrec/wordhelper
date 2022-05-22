from flask import Flask
import re
from flask import request


words = []
new_words = []

with open('svenska-ord.txt','r', encoding='utf-8') as f:
    lines = f.readlines()

def validate():
    words.clear()
    from app import request
    form = request.form.getlist('text')
    for v in form: 
        if v == '':
            words.append(".")
        else:
            words.append(v.lower())

def wordsearch():
    new_words.clear()
    pattern = f'^{words[0]}{words[1]}{words[2]}{words[3]}{words[4]}{words[5]}$'
    for line in lines:
        if re.findall(pattern, line.rstrip('\n')):
            line = new_words.append(line.rstrip('\n'))


def truncatelist():
    if len(new_words) >= 25:
        del new_words[25:]


def containsletters():
    form = request.form['contains']
    letters = form
    for line in lines:
        if form & set(line):
            print(line)


# letters = set('aqk')

# for word in wordlist:
#     if letters & set(word):
#         print word
