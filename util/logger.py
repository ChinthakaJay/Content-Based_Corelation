import logging
from logging.handlers import TimedRotatingFileHandler

from util.config_loader import config

log_config = config['LOG']

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(funcName)s %(process)d %(thread)d %(message)s')

log_handler = TimedRotatingFileHandler(log_config['path'] + '/application.log', when='midnight', backupCount=10)
log_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


def get_logger(name: str = None):
    logger = logging.getLogger(name)
    logger.setLevel(log_config['level'])
    logger.addHandler(log_handler)
    logger.addHandler(console_handler)
    return logger
