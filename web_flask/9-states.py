#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import *
from models import storage
import os
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.teardown_appcontext
def storage_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/states')
def state_list():
    """
        method to render states
    """
    states = storage.all('State').values()
    return render_template(
        "9-states.html",
        states=states,
        condition="states_list")

@app.route('/states/<id>')
def states_id(id):
    """
        method to render state ids
    """
    state_all = storage.all('State')
    try:
        state_id = state_all[id]
        return render_template(
            '9-states.html',
            state_id=state_id,
            condition="state_id")
    except:
        return render_template('9-states.html', condition="not_found")

if __name__ == '__main__':
    app.run(host=host, port=port)
