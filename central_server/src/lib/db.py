import config
from sqlalchemy import create_engine
#import logging

#logger = logging.getLogger(__name__)

"""
Exports an  sqlalchemy connection
"""
def connect():
    connection = create_engine(config.env['CONN_STRING'])
    print('Connection made to database')
    # logger.info('Connection made to database')
    return connection

