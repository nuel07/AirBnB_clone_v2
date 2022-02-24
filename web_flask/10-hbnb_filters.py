#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import *
from models import storage
import os
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '0.0.0.0'
port = 5000

def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/hbnb_filters')
def filters_list():
    """
        method to display html page 6-index.html
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host=host, port=port)
