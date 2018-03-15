import config
import logging


def setup_custom_logger(name):
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        filename=config.env['LOG_FILE_LOCATION']+config.env['LOG_FILE_NAME'],
                        level=logging.DEBUG)
    logger = logging.getLogger(name)
    return logger
