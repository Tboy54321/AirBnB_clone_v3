#!/usr/bin/python3

"""
app_views creation
"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status function"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each object by type"""
    stats = {}

    classes = ["Amenity", "City", "Place", "Review", "State", "User"]

    for cls in classes:
        stats[cls] = storage.count(cls)

    return jsonify(stats)
