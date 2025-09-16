
import logging

logger=logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)

#set console handler
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s",
                            "%d/%m/%Y %I:%M:%S %p")
#set formatter to console handler
console_handler.setFormatter(formatter)

#add console handler to logger
logger.addHandler(console_handler)

#use custom logger
logger.critical("This is is a critical message")
logger.error("This is is a error message")
logger.warning("This is is a warning message")
logger.debug("This is is a debug message")





