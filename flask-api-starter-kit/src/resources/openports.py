"""
Define the REST verbs relative to the device
"""

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import OpenPortsRepository
from util import parse_params


class OpenPortsResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/openPorts/GET.yml')
    def get(_id):
        """ Return openPorts key information based on deviceId """
        openPorts = OpenPortsRepository.get(deviceId=deviceId)
        return jsonify({'openPorts': openPorts.json})

    # @staticmethod
    # @parse_params(
    #     Argument(
    #         'age',
    #         location='json',
    #         required=True,
    #         help='The age of the user.'
    #     ),
    # )
    @swag_from('../swagger/openPorts/POST.yml')
    def post(_id, protocol, local_address, foreign_address, state, program_name, deviceId):
        """ Create an openPorts based on the sent information """
        openPorts = OpenPortsRepository.create(
            _id=_id,
            protocol=protocol,
            local_address=local_address,
            foreign_address=foreign_address,
            state=state,
            program_name=program_name,
            deviceId=deviceId
        )
        return jsonify({'openPorts': openPorts.json})

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
