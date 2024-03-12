"""
Домашнее задание №5
Первое веб-приложение

"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='views')


@app.route("/about/")
def hello_world():
    return render_template('about.tmpl')


@app.route("/")
def root():
    return render_template('index.tmpl')
