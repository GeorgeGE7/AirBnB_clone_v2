#!/usr/bin/python3
"""
two routes and flask init
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home route with simple string"""
    return 'Hello HBNB!'
app.route("/hbnb", strict_slashes=False)
def hbnb():
    """seconde route for hbnb"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')