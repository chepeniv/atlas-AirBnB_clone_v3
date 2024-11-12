#!/usr/bin/python3
'''
a view for `State` objects that handles
all default ESTful API actions
'''

from api.v1.views import app_views, valid_models
from api.v1.views.service_calls import *
from flask import request


StateClass = valid_models().get('State')


@app_views.route(
    '/states',
    methods=['GET'],
    strict_slashes=False)
def get_states():
    '''
    returns json list of all states
    '''
    return get_all_objects(StateClass)


@app_views.route(
    '/states/<state_id>',
    methods=['GET'],
    strict_slashes=False)
def get_state(state_id):
    '''
    returns json dict state found provided state_id
    if not such state exist 404 error is raised
    '''
    return get_single_object(StateClass, state_id)


@app_views.route(
    '/states/<state_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_state(state_id):
    '''
    deletes the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    return delete_object(StateClass, state_id)


@app_views.route(
    '/states',
    methods=['POST'],
    strict_slashes=False)
def create_state():
    '''
    creates a new state object from the provided json
    if successful a json representation is returned
    '''
    return create_object(request, StateClass)


@app_views.route(
    '/states/<state_id>',
    methods=['PUT'],
    strict_slashes=False)
def update_state(state_id):
    '''
    updates the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    return update_object(request, StateClass, state_id)
