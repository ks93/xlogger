# core
import logging
import logging.config
import os

# internal
from .config import config

# initialise logger
log_type = 'production'
log_name = config['handlers']['file']['filename']
if not os.path.exists(os.path.dirname(log_name)):
        os.makedirs(os.path.dirname(log_name))
logging.config.dictConfig(config)
logger = logging.getLogger(log_type)

def update_config():
    log_name = config['handlers']['file']['filename']
    if not os.path.exists(os.path.dirname(log_name)):
            os.makedirs(os.path.dirname(log_name))
    logging.config.dictConfig(config)
    logger = logging.getLogger(log_type)

def set_production():
    log_type = 'production'
    update_config()

def set_development():
    log_type = 'development'
    update_config()
