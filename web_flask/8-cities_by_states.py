#!/usr/bin/python3
'''
task 9 - cities by states
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


# loading cities of state :
    # for DBStorage use relationship cities
    # otherwise use getter cities
# after each request remove the sqlalchemy session
# routes:
    # /cities_by_states
    # H1 - States
    # UL - listing all states sorted by name
        # LI - state.id: <b>state.name</b>
        # UL - cities of state sorted by name
            # LI - city.id: <b>city.name<b>

def by_name(pair):
    '''
    function to indicate to .sort()
    '''
    return pair[0]


def get_sorted_states():
    '''
    returns a sorted list of value pairs containing a name and id each
    '''
    state_names = []
    states = storage.all(State).values()

    if len(states) == 0:
        return None

    for state in states:
        state_names.append((state.name, state.id))

    state_names.sort(key=by_name)
    return state_names

def get_state_cities(state):
    if storage_type == 'db':
        pass
    else:
        pass

@app.route("/states_list", strict_slashes=False)
def list_all_states():
    '''
    serves a template that displays all State objects by name in alphabetical
    order
    '''
    state_names = get_sorted_states()
    if State:
        return render_template("7-states_list.html", states=state_names)
    else:
        abort(404)


@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
