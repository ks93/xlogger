# core
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Set up logging.
default_log_dir = 'logs/'
log_name = os.path.join(os.getenv('LOG_FILE_PATH', default_log_dir),'app.log')

if default_log_dir in log_name:
    if not os.path.exists(log_name):
        os.makedirs(os.path.dirname(log_name))

logger = logging.getLogger(log_name)
logger.setLevel(logging.DEBUG)
# Logging information to specified file.
log_file_handler = TimedRotatingFileHandler(log_name, when = 'midnight', interval = 1)
log_file_handler.setLevel(os.getenv('LOG_LEVEL_FILE', 'DEBUG'))
log_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s'))
# Prints logging information to console.
log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(os.getenv('LOG_LEVEL_CONSOLE', 'DEBUG'))
log_console_handler.setFormatter(logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s'))
logger.addHandler(log_file_handler)
logger.addHandler(log_console_handler)
