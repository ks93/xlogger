# core
import logging
import logging.config
import json
import os
from utils.json_parse import extract_keys

configration_file = 'default_logging.conf'

def configure_logger(configration_file_path, logger_name):
    # load the json object from logging configuration file.
    configuration_dict = dict()
    with open(configration_file_path) as file:
        configuration_dict = json.load(file)

    # Can be multiple filename in the configuration. Now currently only selects the first one.
    path_to_logs = extract_keys(configuration_dict, 'filename')
    log_name = str(path_to_logs[0])

    # make the log directory if it does not exist.
    if not os.path.exists(os.path.dirname(log_name)):
        os.makedirs(os.path.dirname(log_name))
    logging.config.dictConfig(configuration_dict)
    
    return logging.getLogger(logger_name)

logger = configure_logger(configration_file, 'development')
