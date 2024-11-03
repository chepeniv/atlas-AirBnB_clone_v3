#!/usr/bin/python3
'''
task 8 - list of states
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


def by_name(state):
    '''
    function to indicate to .sort()
    '''
    return state.name


def get_sorted_states():
    '''
    returns a sorted list of value pairs containing a name and id each
    '''
    state_names = []
    states = storage.all(State).values()

    if len(states) == 0:
        return None

    for state in states:
        state_names.append(state)

    state_names.sort(key=by_name)
    return state_names


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
