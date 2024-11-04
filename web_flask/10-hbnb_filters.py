#!/usr/bin/python3
'''
task 10 - hbnb filters
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)

# update class .popover in 6-filters.css
#       enable scrolling and set max height of 300px
# all loaded objects will be loaded from DBStorage and must be
#       sorted alphabetically by name
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    '''
    serves a template that displays a single State denoted by its id as well as
    all of its cities in alphabetical order
    '''
    states = storage.all(State).values()

    state = None
    for s in states:
        if s.id == idnum:
            state = s
            break

    if state is not None:
        return render_template("9-states.html", states=[state], single=True)
    else:
        return render_template("9-states.html", states=[], single=False)


@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
