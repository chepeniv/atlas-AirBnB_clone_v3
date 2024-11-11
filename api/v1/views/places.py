# #!/usr/bin/python3
# """
# Handles app_views for places class
# """
# # from models import storage
# from models.place import Place
# from flask import jsonify, abort, request
# from api.v1.views import app_views, storage


# @app_views.route('/places', methods=['GET', 'POST'], strict_slashes=False)
# def get_post_amenities():
#     """returns json list of all places in storage or returns new place"""
#     if request.method == 'GET':
#         places = []
#         for place in storage.all(Place).values():
#             places.append(place.to_dict())
#         return jsonify(places)
#     elif request.method == 'POST':
#         if request.is_json:
#             req = request.get_json()  # or request.form.get('name')
#             email = req.get('email')
#             password = req.get('password')
#             if email:
#                 if password:
#                     new_user = Place(**req)
#                     new_user.save()
#                     return jsonify(new_user.to_dict()), 201
#                 else:
#                     abort(400, description='Missing password')
#             else:
#                 abort(400, description='Missing email')
#         else:
#             abort(400, description='Not a JSON')


# @app_views.route('/places/<user_id>', methods=['GET', 'DELETE', 'PUT'],
#                  strict_slashes=False)
# def get_user_id(user_id):
#     """retrieves, deletes, or updates json'd place object"""
#     if request.method == 'GET':
#         place = storage.get(Place, user_id)
#         if place:
#             return jsonify(place.to_dict())
#         else:
#             abort(404)
#     elif request.method == 'DELETE':
#         place = storage.get(Place, user_id)
#         if place:
#             storage.delete(place)
#             return jsonify({}), 200
#         else:
#             abort(404)
#     elif request.method == 'PUT':
#         place = storage.get(Place, user_id)
#         if place:
#             if request.is_json:
#                 update_dict = request.get_json()
#                 update_dict = {key: value for key, value
#                                in update_dict.items() if key not in
#                                ['id', 'email', 'created_at', 'updated_at']}
#                 for key, value in update_dict.items():
#                     setattr(place, key, value)
#                 place.save()
#                 return jsonify(place.to_dict()), 200
#             else:
#                 abort(400, description='Not a JSON')
#         else:
#             abort(404)
