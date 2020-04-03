config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "advanced":{
            "format":"%(asctime)s.%(msecs)03d - %(module)s - %(process)s - %(name)s - %(threadName)s - %(levelname)s - %(module)s - %(funcName)s:%(lineno)d - %(message)s",
            "datefmt":"%d/%m/%Y %H:%M:%S"
        },
        "csv":{
            "format":"%(asctime)s.%(msecs)03d,%(module)s,%(process)s,%(name)s,%(threadName)s,%(levelname)s,%(module)s,%(funcName)s:%(lineno)d,%(message)s",
            "datefmt":"%d/%m/%Y %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "advanced"
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "advanced",
            "filename": "logs/app.log",
            "when": "midnight",
            "interval": 1
        }
    },
    "loggers": {
        "development": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
        },
        "production": {
            "level": "INFO",
            "handlers": ["file"]
        }
    }
}