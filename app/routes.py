from app import app
from flask import render_template, request
from app.models import model, formopener
import json
import random


vocab_dict = {}
old_defs = []
#load all vocab from json file
with open("/Users/2020yzhou/Desktop/sat_vocab_CS_IA 2/app/static/majortests_words.json") as json_file:
    data = json.load(json_file)
    #put vocab in dictionary
    for d in data["results"]:
        vocab_dict[d["definition"]] = d["word"]

@app.route('/')
@app.route('/index',methods=['GET', "POST"])
def index():
    score = 0
    #get random vocab word
    definition = random.choice(list(vocab_dict.keys()))
    #get form info
    user_input = dict (request.form)
    if user_input:
        actual_word = vocab_dict.get(str(old_defs[-1]))
        if user_input["user_word"].lower() == actual_word.lower():
            score +=1
        else:
            old_defs.append(definition)
            return render_template("index.html", word = definition, score = score, correct_word = "Correct word: " + actual_word)
    old_defs.append(definition)
    return render_template("index.html", word = definition, score = score)
