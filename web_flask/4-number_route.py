#!/usr/bin/python3
""" start flask web app """
from flask import *
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.route('/')
def hello_hbnb():
    """ display hello text """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ display hbnb """
    return "HBNB"

@app.route('/c/<text>')
def cfun(text):
    """ display c is fun """
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route('/python/<text>')
def pycool(text="is cool"):
    """ display python is cool """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route('/number/<int:n>')
def isnum(n):
    """ display number """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host=host, port=port)
