from lib import db
from flask import abort
# import logging
# logger = logging.getLogger(__name__)


class DumpData:
    def __init__(self):
        self.db = db.connect()

    def save_json(self, json_obj):
        """
        :param json_obj: json 
        :return: void
        """
        try:
            self.db.execute("INSERT INTO network_information (info) VALUES (%s)", json_obj)
        except Exception as e:
            print('Error while inserting')
            msg = 'Not able to insert json object in network_information table ' + str(e)
            error_msg = {'message': msg}
            abort(400, error_msg)

        print("Success dumping")

