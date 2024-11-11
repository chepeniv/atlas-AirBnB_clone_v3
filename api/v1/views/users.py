#!/usr/bin/python3
"""
Handles app_views for amenities class
"""
from models import storage
from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def get_post_amenities():
    """returns json list of all amenities in storage or returns new user"""
    if request.method == 'GET':
        users = []
        for user in storage.all(User).values():
            users.append(user.to_dict())
        return jsonify(users)
    elif request.method == 'POST':
        if request.is_json:
            req = request.get_json()  # or request.form.get('name')
            name = req.get('name')
            email = req.get('email')
            password = req.get('password')
            if name:
                if email:
                    if password:
                        new_user = User(name=name)
                        new_user.save()
                        return jsonify(new_user.to_dict()), 201
                    else:
                        abort(400, description='Missing password')
                else:
                    abort(400, description='Missing email')
            else:
                abort(400, description='Missing name')
        else:
            abort(400, description='Not a JSON')


@app_views.route('/amenities/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_user_id(user_id):
    """retrieves, deletes, or updates json'd user object"""
    if request.method == 'GET':
        user = storage.get(User, user_id)
        if user:
            return jsonify(user.to_dict())
        else:
            abort(404)
    elif request.method == 'DELETE':
        user = storage.get(User, user_id)
        if user:
            storage.delete(user)
            return {}, 200
        else:
            abort(404)
    elif request.method == 'PUT':
        user = storage.get(User, user_id)
        if user:
            if request.is_json:
                update_dict = request.get_json()
                update_dict = {key: value for key, value
                               in update_dict.items() if key not in
                               ['id', 'email', 'created_at', 'updated_at']}
                for key, value in update_dict.items():
                    setattr(user, key, value)
                user.save()
                return jsonify(user.to_dict()), 200
            else:
                abort(400, description='Not a JSON')
        else:
            abort(404)
