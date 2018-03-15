import config
import logging

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    filename=config.env['LOG_FILE_LOCATION']+config.env['LOG_FILE_NAME'],
    level=logging.DEBUG
)