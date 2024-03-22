#!/usr/bin/python3

"""First Route

Returns:
    string: Welcome message
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """Just the first route

    Returns:
        string: welcome message
    """
    return "Hello HBNB!"
