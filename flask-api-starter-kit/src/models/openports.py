"""
Define the OpenPorts model
"""
from . import db
from .abc import BaseModel


class OpenPorts(db.Model, BaseModel):
    """ The OpenPorts model """
    __tablename__ = 'OpenPorts'

    _id = db.Column(db.String(30), primary_key=True, unique=True)
    protocol = db.Column(db.String(300))
    local_address = db.Column(db.String(300))
    foreign_address = db.Column(db.String(300))
    state = db.Column(db.String(300))
    program_name = db.Column(db.String(300))
    deviceId = db.Column(db.String(30), ForeignKey('Device._id'), nullable=False)

    def __init__(self, _id, protocol, local_address, foreign_address, state, program_name, deviceId):
        """ Create a new OpenPorts """
        self._id = _id
        self.protocol = protocol
        self.local_address = local_address
        self.foreign_address = foreign_address
        self.state = state
        self.program_name = program_name
        self.deviceId = deviceId