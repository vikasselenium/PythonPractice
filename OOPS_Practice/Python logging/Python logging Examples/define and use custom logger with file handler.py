
import logging

# get the logger object
logger=logging.getLogger("custom_logger")
# set log level at logger object
logger.setLevel(logging.DEBUG)

#get file handler and set log level at file handler level
file_handler=logging.FileHandler("log_new.txt", mode="a")
file_handler.setLevel(logging.ERROR)

#get a formatter object
formatter=logging.Formatter("%(asctime)s: %(levelname)s : %(name)s, %(message)s",
                           "%d/%m/%Y %I:%M:%S %p")
#set formatter on file handler
file_handler.setFormatter(formatter)

#add file handler to logger
logger.addHandler(file_handler)

#use custom logger
logger.critical("This is a critical message")
logger.error("This is a error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
