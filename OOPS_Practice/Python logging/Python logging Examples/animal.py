import logging
from custlogger import get_custom_logger

logger = get_custom_logger(logging.DEBUG)

class Animal:
    breathing=True

    def __init__(self):
        self.breathing=Animal.breathing


    def can_move(self):
        return True

    def log_messages(self):
        logger.name=self.__class__.__name__
        logger.critical("This is a critical message")
        logger.error("This is a error message")
        logger.warning("This is a warning message")
        logger.info("This is info message")
        logger.debug("This is a debug message")


animal1=Animal()
animal1.log_messages()

