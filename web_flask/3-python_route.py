#!/usr/bin/python3
"""
first route and flask init
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """home route with simple string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns string HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
  """displays C with user input as a params 

  Args:
      text (string): from user params
  """

  return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text= 'is cool'):
  """displays Python with user input as a params 

  Args:
      text (string): from user params
  """

  return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')