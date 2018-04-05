"""
Define the REST verbs relative to the device
"""

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import DeviceRepository
from util import parse_params


class DeviceResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/device/GET.yml')
    def get(_id):
        """ Return an device key information based on id """
        device = DeviceRepository.get(_id=_id)
        return jsonify({'device': device.json})

    # @staticmethod
    # @parse_params(
    #     Argument(
    #         'age',
    #         location='json',
    #         required=True,
    #         help='The age of the user.'
    #     ),
    # )
    @swag_from('../swagger/device/POST.yml')
    def post(_id, name, osinfo, networkDevices, openPorts):
        """ Create an user based on the sent information """
        user = DeviceRepository.create(
            _id=_id,
            name=name,
            osinfo=osinfo
        )
        return jsonify({'device': device.json})

    # @staticmethod
    # @parse_params(
    #     Argument(
    #         'age',
    #         location='json',
    #         required=True,
    #         help='The age of the user.'
    #     ),
    # )
    # @swag_from('../swagger/user/PUT.yml')
    # def put(last_name, first_name, age):
    #     """ Update an user based on the sent information """
    #     repository = UserRepository()
    #     user = repository.update(
    #         last_name=last_name,
    #         first_name=first_name,
    #         age=age
    #     )
    #     return jsonify({'user': user.json})
