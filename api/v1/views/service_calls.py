#!/usr/bin/python3
'''
definition of functions used to process RESTful api request
'''

from models import storage
from flask import request, abort


def get_all_objects(model_class):
    '''
    returns json list of all objects of a given type found in storage
    '''
    objects = storage.all(model_class)
    json_objects = []
    for obj in objects.values():
        json_objects.append(obj.to_dict())
    return json_objects


def get_single_object(model_class, obj_id):
    '''
    returns json dict city found provided city_id
    if not such city exist 404 error is raised
    '''
    obj = storage.get(model_class, obj_id)
    if obj:
        obj = obj.to_dict()
        return obj
    else:
        return abort(404)


def delete_object(model_class, obj_id):
    '''
    deletes the object found via the obj_id
    if not such object exist 404 error is raised
    '''
    obj = storage.get(model_class, obj_id)
    if obj:
        storage.delete(obj)
        storage.save()
        return {}, 200
    else:
        return abort(404)


def create_object(request, model_class):
    '''
    creates a new object from the provided json
    if successful a json representation is returned
    '''
    # might need a bit more work to generalize further
    # that is, likely using kwargs to set object fields
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    if 'name' not in json_data:
        return "Missing name", abort(400)

    name = json_data.get('name')
    new_obj = model_class(name=name)
    if new_obj:
        storage.new(new_obj)
        storage.save()
        return new_obj.to_dict(), 201


def update_object(request, model_class, obj_id):
    '''
    updates the object found via the obj_id
    if not such object exist 404 error is raised
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    obj = storage.get(model_class, obj_id)
    if obj:
        for key, value in json_data.items():
            if (key not in {'id', 'created_at', 'updated_at'}
                    and hasattr(obj, key)):
                setattr(obj, key, value)
        storage.save()
        return obj.to_dict(), 200
    else:
        return abort(404)
