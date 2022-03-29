import re
from flask import request, redirect
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def message():
    print(request.form)
    return render_template("about.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message2():
    if request.method == 'GET':
        print(request.form)
        return(render_template("contact.html"))
    elif request.method == 'POST':
        print(request.form)
        return render_template("contact.html")