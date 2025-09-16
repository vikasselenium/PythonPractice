


import logging
format='%(asctime)s %(levelname)s - %(message)s'




logging.basicConfig(filename="sample.log", level=logging.DEBUG, format=format)

logging.debug("This is debug logging")
logging.info("This is Info logging")
logging.warn("This is warning message")
logging.error("This is error message")


