#!/usr/bin/python3
"""Module that handles users RESTful API"""

from flask import jsonify, abort, request, Response
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def get_users():
    """ focus on all the user objects """

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        if 'email' not in data:
            return Response("Missing email", 400)
        if 'password' not in data:
            return Response("Missing password", 400)
        user = User(email=data.get('email'),
                    password=data.get('password'))
        user.save()
        return jsonify(user.to_dict()), 201

    all_users = storage.all('User')
    users = []

    for user in all_users.values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_user(user_id=None):
    """ focus on just a single user object """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if request.method == 'DELETE':
        storage.delete(user)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        data['id'] = user.id
        data['created_at'] = user.created_at
        user.__init__(**data)
        user.save()
        return jsonify(user.to_dict()), 200

    return jsonify(user.to_dict())
