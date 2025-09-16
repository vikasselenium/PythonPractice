import logging


#levelname: name: message
# more attributes are on python doc portal
print("logging Demo")
#logging.basicConfig(format='%(levelname)s')
#logging.basicConfig(format='%(levelname)s:%(message)s')
logging.basicConfig(format='%(levelname)s:%(name)s:%(process)d:%(message)s:%(module)s:%(lineno)s')
logging.critical("this is a critical message")
logging.error("this is a error message")
logging.warning("this is a warning message")
logging.info("this is a info message")
logging.debug("this is a debug message")