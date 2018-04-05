""" Defines the NetworkDevice repository """

from models import NetworkDevice


class NetworkDeviceRepository:
    """ The repository for the networkDevice model """

    @staticmethod
    def get(deviceId):
        """ Query network devices using deviceId """

        return NetworkDevice.query.filter_by(
        	deviceId=deviceId
        )

    # def update(self, user_name, password, email):
    #     """ Update a user's age """
    #     user = self.get(last_name, first_name)
    #     user.age = age

    #     return user.save()

    @staticmethod
    def create(_id, name, v4addr, v6addr, netmask, hwaddr, deviceId):
        """ Create a new user """
        networkDevice = NetworkDevice(_id=_id, name=name, osinfo=osinfo)

        return networkDevice.save()
