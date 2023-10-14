#!/usr/bin/python3
""" Index view
"""
from flask import jsonify, make_response
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return make_response(jsonify({"status": "OK"}))
