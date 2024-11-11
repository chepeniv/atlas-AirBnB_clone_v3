#!/usr/bin/python3


# `api/v1/views/states.py`
# `api/v1/views/__init__.py`

# create a new view for `State` objects that handles all default RESTful API
# actions

# in `api/v1/views/states.py` :
# - use `to_dict()` to retrieve an object into valid json
# - update `__init__.py` to import this file

# - `GET /api/v1/states` retrieves the list of all states
# - `GET /api/v1/states/<state_id>` retrieves the matching `State` object
# 	- if no match found raise `404`
# - `DELETE /api/v1/states/<state_id>` deletes the matching `State` object
# 	- if successful, return an empty dictionary along with the status code `200`
# 	- if no match found raise `404`
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
