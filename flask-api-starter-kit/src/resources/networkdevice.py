"""
Define the REST verbs relative to the device
"""

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import NetworkDeviceRepository
from util import parse_params


class NetworkDeviceResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/networkDevice/GET.yml')
    def get(_id):
        """ Return networkDevices key information based on deviceId """
        networkDevice = NetworkDeviceRepository.get(deviceId=deviceId)
        return jsonify({'networkDevice': networkDevice.json})

    # @staticmethod
    # @parse_params(
    #     Argument(
    #         'age',
    #         location='json',
    #         required=True,
    #         help='The age of the user.'
    #     ),
    # )
    @swag_from('../swagger/networkDevice/POST.yml')
    def post(_id, name, v4addr, v6addr, netmask, hwaddr, deviceId):
        """ Create an networkDevice based on the sent information """
        networkDevice = NetworkDeviceRepository.create(
            _id=_id,
            name=name,
            v4addr=v4addr,
            v6addr=v6addr,
            netmask=netmask,
            hwaddr=hwaddr,
            deviceId=deviceId
        )
        return jsonify({'networkDevice': networkDevice.json})

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
