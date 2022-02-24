#!/usr/bin/python3
""" start flask web app """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '0.0.0.0'
port = 5000

@app.route('/')
def hello_hbnb():
    """ display hello text """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ diplay hbnb """
    return "HBNB"

@app.route('/c/<text>')
def cfun(text):
    """ display c is fun """
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host=host, port=port)
