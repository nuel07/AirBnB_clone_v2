#!/usr/bin/python3
''' start flask web app '''
from flask import *
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def db_teardown(self):
    """
        handle teardown
    """
    storage.close()

@app.route('/states_list')
def state_list():
    """
        display HTML page
    """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host=port, port=port)
