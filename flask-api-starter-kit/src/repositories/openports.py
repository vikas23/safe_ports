""" Defines the NetworkDevice repository """

from models import OpenPorts


class OpenPortsRepository:
    """ The repository for the openports model """

    @staticmethod
    def get(deviceId):
        """ Query open ports using deviceId """

        return OpenPorts.query.filter_by(
        	deviceId=deviceId
        )

    # def update(self, user_name, password, email):
    #     """ Update a user's age """
    #     user = self.get(last_name, first_name)
    #     user.age = age

    #     return user.save()

    @staticmethod
    def create(_id, protocol, local_address, foreign_address, state, program_name, deviceId):
        """ Create a new user """
        openPorts = OpenPorts(_id=_id, protocol=protocol, local_address=local_address, foreign_address=foreign_address, state=state, program_name=program_name, deviceId=deviceId)

        return openPorts.save()
