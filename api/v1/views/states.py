#!/usr/bin/python3
'''
a view for `State` objects that handles
all default ESTful API actions
'''

from api.v1.views import app_views, storage, valid_models
from flask import request, abort


state_class = valid_models().get('State')


@app_views.route(
    '/states',
    methods=['GET'],
    strict_slashes=False)
def get_states():
    '''
    returns json list of all states
    '''
    states = storage.all(state_class)
    json_states = []
    for state in states.values():
        json_states.append(state.to_dict())
    return json_states


@app_views.route(
    '/states/<state_id>',
    methods=['GET'],
    strict_slashes=False)
def get_state(state_id):
    '''
    returns json dict state found provided state_id
    if not such state exist 404 error is raised
    '''
    state = storage.get(state_class, state_id)
    if state:
        state = state.to_dict()
        return state
    else:
        return abort(404)


@app_views.route(
    '/states/<state_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_state(state_id):
    '''
    deletes the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    state = storage.get(state_class, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return {}, 200
    else:
        return abort(404)


@app_views.route(
    '/states',
    methods=['POST'],
    strict_slashes=False)
def create_state():
    '''
    creates a new state object from the provided json
    if successful a json representation is returned
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    if 'name' not in json_data:
        return "Missing name", abort(400)

    name = json_data.get('name')
    new_state = state_class(name=name)
    if new_state:
        storage.new(new_state)
        storage.save()
        return new_state.to_dict(), 201


@app_views.route(
    '/states/<state_id>',
    methods=['PUT'],
    strict_slashes=False)
def update_state(state_id):
    '''
    updates the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    state = storage.get(state_class, state_id)
    if state:
        for key, value in json_data.items():
            if (key not in {'id', 'created_at', 'updated_at'}
                    and hasattr(state, key)):
                setattr(state, key, value)
        storage.save()
        return state.to_dict(), 200
    else:
        return abort(404)
