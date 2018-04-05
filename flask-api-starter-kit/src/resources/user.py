"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/user/GET.yml')
    def get(user_name, user_email):
        """ Return an user key information based on his name """
        user = UserRepository.get(user_name=user_name, user_email=user_email)
        return jsonify({'user': user.json})

    # @staticmethod
    # @parse_params(
    #     Argument(
    #         'age',
    #         location='json',
    #         required=True,
    #         help='The age of the user.'
    #     ),
    # )
    @swag_from('../swagger/user/POST.yml')
    def post(user_email, user_name, password, is_safe):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            user_name=user_name,
            user_email=user_email,
            age=age,
            is_safe=is_safe
        )
        return jsonify({'user': user.json})

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
