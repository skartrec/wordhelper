from flask import Flask
import re

words = []
new_words = []

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
    from app import request
    new_words.clear()
    file = open('svenska-ord.txt', encoding='utf-8')
    pattern = f'^{words[0]}{words[1]}{words[2]}{words[3]}{words[4]}{words[5]}$'
    for line in file.readlines():
        if re.findall(pattern, line.rstrip('\n')):
            line = new_words.append(line.rstrip('\n'))

def exclude(list):
    from app import request
    exclude = request.form['exclude']
    excluded_words =  [ele for ele in new_words if all(ch not in ele for ch in exclude)]
    print(excluded_words)


def truncatelist():
    if len(new_words) >= 25:
        del new_words[25:]

# def exclude_letters():
#     from app import request
#     exclude = request.form['exclude']
#     excluded_words =  [ele for ele in new_words if all(ch not in ele for ch in exclude)]

