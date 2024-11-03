#!/usr/bin/python3
'''
task 7 - list of states

'''

import sys
sys.path.append('../')
from models import storage, storage_type
from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''
    serve text, upon request, to route /
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    serve text, upon request, to route /hbnb
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''
    process the given url and serve the resulting text on route /c/<text>
    '''
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    '''
    process the given url and serve the resulting text on route /python/<text>
    '''
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    '''
    process the given url and output the result on route /number/<n>
    '''
    if n.isdecimal():
        n = int(n)
        return f"{n} is a number"
    else:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    '''
    return a dynamic template webpage based on the url
    '''
    if n.isdecimal():
        n = int(n)
        return render_template("5-number.html", number=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_even_template(n):
    '''
    returns a template that determines whether a number is even or not
    '''
    if n.isdecimal():
        n = int(n)
        odd = n % 2
        return render_template("6-number_odd_or_even.html", number=n, odd=odd)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
