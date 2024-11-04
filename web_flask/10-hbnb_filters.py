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

# /hbnb_filters
# duplicate 6-index.html into templates/10-hbnb_filters.html
#       replace content of H4 under each filter title (H3 states and H3
#       amenities)by &nbsp;
# into web_flask/static/styles
#       copy 3-footer.css, 3-header.css, 4-common.css, 6-filters.css
#       update class .popover in 6-filters.css
#           enable scrolling and set max height of 300px
# into web_flask/static/images
#       copy icon.png, logo.png,
# all loaded objects (states, cities, and amenities) will be loaded from
#       DBStorage and must be sorted alphabetically by name
@app.route("/states", strict_slashes=False)
def all_states():
    '''
    serves a template that displays all State objects by name in alphabetical
    order
    '''
    states = storage.all(State).values()
    states = list(states)
    if len(states) > 0:
        return render_template("9-states.html", states=states, single=False)
    else:
        abort(404)


# determine how a state with no cities should be displayed
@app.route("/states/<idnum>", strict_slashes=False)
def state_by_id(idnum):
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
