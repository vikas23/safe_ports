"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import DeviceResource


DEVICE_BLUEPRINT = Blueprint('device', __name__)
Api(DEVICE_BLUEPRINT).add_resource(
    DeviceResource,
    '/device/<string:_id>'
)
