#!/usr/bin/python3
'''
a view for `State` objects that handles
all default ESTful API actions
'''

from api.v1.views import app_views, storage, valid_models
from flask import request


state_class = valid_models().get('State')


@app_views.route('/states', methods=['GET'])
def get_states():
    '''
    returns json list of all states
    '''
    states = storage.all(state_class)
    json_states = []
    for state in states.values():
        json_states.append(state.to_dict())
    return json_states


@app_views.route('/states/<state_id>', methods=['GET'])
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


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''
    deletes the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    state = storage.get(state_class, state_id)
    if state:
        storage.delete(state)
        storage.save()
        storage.reload()
        return {}, 200
    else:
        return abort(404)


@app_views.route('/states', methods=['POST'])
def post_state():
    '''
    creates a new state object from the provided json
    if successful a json representation is returned
    '''
    json_data = request.get_json()
    if not json_data:
        return "Not a JSON", abort(400)
    if not 'name' in json_data:
        return "Missing name", abort(400)

    name = json_data.get('name')
    new_state = state_class(name=name)
    if new_state:
        storage.new(new_state)
        storage.save()
        return new_state.to_dict(), 201


# - `PUT /api/v1/states/<state_id>` updates a `State` object
# 	- if `state_id` is invalid raise `404` error
# 	- use `request.get_json` from flask to transform the http body request to
# 	  dictionary
# 	- if the http body is not valid json raise a `400` error with the message
# 	  `Not a JSON`
# 	- update the `State` object with all key-value pairs of the dictionary
# 	- ignore the keys: `id`, `created_at`, and `updated_at`
# 	- return the `State` object with the code `200`
