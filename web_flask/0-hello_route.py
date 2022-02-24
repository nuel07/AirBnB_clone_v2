#!/usr/bin/python3
""" starts flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.route('/')
def hello_hbnb():
    """ display text """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host=host, port=port)
