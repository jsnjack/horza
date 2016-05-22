import os


class Settings(object):
    BASE_DIR = os.path.dirname(__file__)

    DB_PATH = os.path.join(os.path.expanduser("~"), ".horza")
    DB_URL = "sqlite:///%s/horza.sqlite3" % DB_PATH
    DB_ECHO = True

    # Interface
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 550

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,

        # How to format the output
        'formatters': {
            'standard': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': "%(message)s"
            }
        },

        # Log handlers (where to go)
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'horza.log_handler.ColorizingStreamHandler',
                'formatter': 'standard'
            },
        },

        # Loggers (where does the log come from)
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'install': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False
            },
            'requests': {
                'handlers': ['console'],
                'level': 'WARN',
            }
        }
    }
