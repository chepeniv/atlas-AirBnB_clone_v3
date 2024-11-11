#!/usr/bin/python3
'''
a view for `State` objects that handles
all default ESTful API actions
'''

from api.v1.views import app_views, storage, valid_models
from flask import jsonify


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
    return jsonify(json_states)


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
    returns json dict state found provided state_id
    if not such state exist 404 error is raised
    '''
    state = storage.get(state_class, state_id)
    if state:
        storage.delete(state)
        storage.save()
        storage.reload()
        return {}, 200
    else:
        # if no match found raise `404`
        return abort(404)



# - `POST /api/v1/states` create a `State` object
# 	- use `request.get_json` from Flask to transform the http body request
# 	  to a dictionary
# 	- if invalid json is provided raise a `400` error with the message
# 	  `Not a JSON`
# 	- if the key `name` isn't provided raise a `400` error with the message
# 	  `Missing name`
# 	- if successful return a new `State` with the status code `201`

# - `PUT /api/v1/states/<state_id>` updates a `State` object
# 	- if `state_id` is invalid raise `404` error
# 	- use `request.get_json` from flask to transform the http body request to
# 	  dictionary
# 	- if the http body is not valid json raise a `400` error with the message
# 	  `Not a JSON`
# 	- update the `State` object with all key-value pairs of the dictionary
# 	- ignore the keys: `id`, `created_at`, and `updated_at`
# 	- return the `State` object with the code `200`
