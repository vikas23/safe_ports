"""
Define the User model
"""
from . import db
from .abc import BaseModel


class User(db.Model, BaseModel):
    """ The User model """
    __tablename__ = 'user'

    user_name = db.Column(db.String(300), primary_key=True, unique=True)
    user_email = db.Column(db.String(300), primary_key=True, unique=True)
    password = db.Column(db.String(300))
    is_safe = db.Column(db.Boolean(create_constraint=False), nullable=True)

    def __init__(self, user_name, user_email, password, is_safe):
        """ Create a new User """
        self.user_name = user_name
        self.user_email = user_email
        self.password = password
        self.is_safe = is_safe