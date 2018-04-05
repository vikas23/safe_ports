"""
Define the NetworkDevice model
"""
from . import db
from .abc import BaseModel


class NetworkDevice(db.Model, BaseModel):
    """ The NetworkDevice model """
    __tablename__ = 'NetworkDevice'

    _id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(300))
    v4addr = db.Column(db.String(300))
    v6addr = db.Column(db.String(300))
    netmask = db.Column(db.String(300))
    hwaddr = db.Column(db.String(300))
    deviceId = db.Column(db.String(30), ForeignKey('Device._id'), nullable=False)

    def __init__(self, _id, name, v4addr, v6addr, netmask, hwaddr, deviceId):
        """ Create a new NetworkDevice """
        self._id = _id
        self.name = name
        self.v4addr = v4addr
        self.v6addr = v6addr
        self.netmask = netmask
        self.hwaddr = hwaddr
        self.deviceId = deviceId