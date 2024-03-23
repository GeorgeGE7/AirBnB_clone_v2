#!/usr/bin/python3
"""
Flask application with db connection to get states
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def state_with_id(state_id=None):
    """get all states ordered..."""
    states = storage.all("State")
    if state_id:
        state_id = f"State.{state_id}"
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """tearing down with reloading the storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')