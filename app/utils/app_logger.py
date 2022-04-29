import sys
import logging
from app.utils.decorators import singleton
from logging.handlers import RotatingFileHandler

@singleton
class AppLogger:

    def __init__(self,**kwargs):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)

        file_handler = RotatingFileHandler(kwargs.get('log_filename'),
                                           mode='a',
                                           maxBytes=5 * 1024 * 1024,
                                           backupCount=2,
                                           encoding=None,
                                           delay=0)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stdout_handler)

    def message_handle(self, **kwargs):
        """
        this is the logging/message handler function for the entire application
        :param kwargs: here the kwargs contains `msg` param that contains the message as string :TODO add params for type/severity
        :return: N/A
        """
        debug_level = kwargs.get("level", "info")
        if debug_level == "info":
            self.logger.info(kwargs.get("msg"))
        if debug_level == "error":
            self.logger.error(kwargs.get("msg"))


_log_message_ = AppLogger(log_filename='logs.log')