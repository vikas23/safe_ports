"""
Define the Device model
"""
from . import db
from .abc import BaseModel


class Device(db.Model, BaseModel):
    """ The Device model """
    __tablename__ = 'Device'

    _id = db.Column(db.String(100), primary_key=True, unique=True)
    name = db.Column(db.String(300))
    osinfo = db.Column(db.String(300))
    networkDevices = db.relationship("NetworkDevice")
    openPorts = db.relationship("OpenPorts")

    def __init__(self, _id, name, osinfo, networkDevices, openPorts):
        """ Create a new Device """
        self._id = _id
        self.name = name
        self.osinfo = osinfo
        self.networkDevices = networkDevices
        self.openPorts = openPorts