""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(user_name, password):
        """ Query a user_name and password """
        return User.query.filter_by(
            user_name=user_name,
            password=password
        ).one()

    # def update(self, user_name, password, email):
    #     """ Update a user's age """
    #     user = self.get(last_name, first_name)
    #     user.age = age

    #     return user.save()

    @staticmethod
    def create(user_name, password, user_email, is_safe):
        """ Create a new user """
        user = User(user_name=user_name, password=password, is_safe=is_safe, user_email=user_email)

        return user.save()
