
import logging.config

from config import LOG_DIR, LOG_FORMAT, LOG_HANDLERS, LOG_LEVEL, LOG_TIME_FORMAT

# Create logger folder
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Logger configuration
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': LOG_FORMAT,
            'datefmt': LOG_TIME_FORMAT
        },
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': LOG_DIR / 'file.log',
            'maxBytes': 15_728_640,     # 15M * 1024K * 1024B
            'backupCount': 10,
        },
    },
    'loggers': {
        'log': {
            'handlers': LOG_HANDLERS,
            'level': LOG_LEVEL,
            'propagate': True,
        }
    },
}
logging.config.dictConfig(config=LOG_CONFIG)

# Default logger
logger = logging.getLogger('log')
