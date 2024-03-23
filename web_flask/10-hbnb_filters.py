#!/usr/bin/python3
"""
Flask application with db connection to fillter
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def get_with_filter():
    """get data and filter then display it"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """Tearing down"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')