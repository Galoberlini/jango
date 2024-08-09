from .dir import *
import logging.config


# Logging

log_path = DIR_PRE_APP.child('logs')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'log_message': {
            '()': 'colorlog.ColoredFormatter',
            'log_colors': {
                'DEBUG': 'bold_black',
                'INFO': 'white',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
            'format': '%(levelname)s_%(asctime)s_%(module)s: %(message)s#]',
            'datefmt': "%Y-%m-%dT%H:%M:%S"
        }
    },
    'handlers': {
        'info': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'log_message',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'log_message',
        },
        'log_error': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'M',
            'interval': 1,
            'filename': f'{log_path}/warning.log',
            'formatter': 'log_message',
        },
    },
    'root': {
        'handlers': ['info', 'error', 'log_error'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'loggers': {
        'django': {
            'handlers': ['info', 'log_error'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

logging.config.dictConfig(LOGGING)
