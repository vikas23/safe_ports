""" Defines the Device repository """

from models import Device


class DeviceRepository:
    """ The repository for the user model """

    @staticmethod
    def get(_id):
        """ Query a user_name and password """
        return Device.query.filter_by(
        	_id=_id
        ).one()

    # def update(self, user_name, password, email):
    #     """ Update a user's age """
    #     user = self.get(last_name, first_name)
    #     user.age = age

    #     return user.save()

    @staticmethod
    def create(_id, name, osinfo):
        """ Create a new user """
        device = Device(_id=_id, name=name, osinfo=osinfo)

        return device.save()
