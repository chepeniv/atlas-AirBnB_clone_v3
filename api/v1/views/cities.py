#!/usr/bin/python3
'''
a view for `City` objects that handles
all default RESTful API actions
'''

from api.v1.views import app_views, valid_models
from api.v1.views.service_calls import *


CityClass = valid_models().get('City')
StateClass = valid_models().get('State')


@app_views.route(
    'states/<state_id>/cities',
    methods=['GET'],
    strict_slashes=False)
def get_cities(state_id):
    '''
    returns json list of all cities found for a given state
    '''
    return get_all_objects_from(StateClass, state_id, 'cities')


@app_views.route(
    '/cities/<city_id>',
    methods=['GET'],
    strict_slashes=False)
def get_city(city_id):
    '''
    returns json dict city found provided city_id
    if not such city exist 404 error is raised
    '''
    return get_single_object(CityClass, city_id)


@app_views.route(
    '/cities/<city_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_city(city_id):
    '''
    deletes the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    return delete_object(CityClass, city_id)


@app_views.route(
    'states/<state_id>/cities',
    methods=['POST'],
    strict_slashes=False)
def create_city(state_id):
    '''
    creates a new city object from the provided json
    if successful a json representation is returned
    '''
    return create_object_for(
        parent=StateClass,
        child=CityClass,
        required=['name'],
        parent_id={'state_id': state_id})


@app_views.route(
    '/cities/<city_id>',
    methods=['PUT'],
    strict_slashes=False)
def update_city(city_id):
    '''
    updates the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    return update_object(CityClass, city_id)
