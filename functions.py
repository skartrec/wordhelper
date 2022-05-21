from flask import Flask
import re



# complete_words = [x for x in words if len(x) <= 6]
words = []
new_words = []

def validate():
    words.clear()
    from app import request
    form = request.form
    for v in form.values(): 
        print(v)
        if v == '':
            words.append(".")
        else:
            words.append(v.lower())
    print(words) 

def wordsearch():
    new_words.clear()
    print(new_words)
    file = open('svenska-ord.txt', encoding='utf-8')
    pattern = f'^{words[0]}{words[1]}{words[2]}{words[3]}{words[4]}{words[5]}$'
    for line in file.readlines():
        if re.findall(pattern, line.rstrip('\n')):
            line = new_words.append(line.rstrip('\n'))
            print(new_words)

def truncatelist():
    if len(new_words) >= 25:
        del new_words[25:]

