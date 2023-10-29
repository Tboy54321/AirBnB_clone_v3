#!/usr/bin/python3

from flask import jsonify, request, abort
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    amenity = [amenity.to_dict() for amenity in storage.all(Amenity).values()]
    return jsonify(amenity)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenities_by_id(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    if 'name' not in request_data:
        abort(400, 'Missing name')
    new_amenity = Amenity(**request_data)
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in request_data.items():
        if key not in ignore:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
