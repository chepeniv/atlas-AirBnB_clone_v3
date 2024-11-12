#!/usr/bin/python3
'''
a view for `City` objects that handles
all default RESTful API actions
'''

from api.v1.views import app_views, storage, valid_models
from flask import request, abort


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
    state = storage.get(StateClass, state_id)
    if state:
        cities = state.cities
        json_cities = []
        for city in cities:
            json_cities.append(city.to_dict())
        return json_cities
    else:
        return abort(404)


@app_views.route(
    '/cities/<city_id>',
    methods=['GET'],
    strict_slashes=False)
def get_city(city_id):
    '''
    returns json dict city found provided city_id
    if not such city exist 404 error is raised
    '''
    city = storage.get(CityClass, city_id)
    if city:
        city = city.to_dict()
        return city
    else:
        return abort(404)


@app_views.route(
    '/cities/<city_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_city(city_id):
    '''
    deletes the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    city = storage.get(CityClass, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return {}, 200
    else:
        return abort(404)


@app_views.route(
    'states/<state_id>/cities',
    methods=['POST'],
    strict_slashes=False)
def create_city(state_id):
    '''
    creates a new city object from the provided json
    if successful a json representation is returned
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    if 'name' not in json_data:
        return "Missing name", abort(400)

    state = storage.get(StateClass, state_id)
    if not state:
        return abort(404)

    name = json_data.get('name')
    new_city = CityClass(name=name, state_id=state_id)
    if new_city:
        storage.new(new_city)
        storage.save()
        return new_city.to_dict(), 201


@app_views.route(
    '/cities/<city_id>',
    methods=['PUT'],
    strict_slashes=False)
def update_city(city_id):
    '''
    updates the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    city = storage.get(CityClass, city_id)
    if city:
        for key, value in json_data.items():
            if (key not in {'id', 'created_at', 'updated_at'}
                    and hasattr(city, key)):
                setattr(city, key, value)
        storage.save()
        return city.to_dict(), 200
    else:
        return abort(404)