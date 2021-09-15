import logging

class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a+', encoding="windows-1251") as file:
            file.write(message + '\n')

logger_config = {
    'version':1,
    'disable_existing_loggers':False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'std_format'
        },
        'file': {
            '()': MegaHandler,
            'level': 'INFO',
            'filename': 'bank_operations.log',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'INFO',
            'handlers': ['file']
        }
    }
}