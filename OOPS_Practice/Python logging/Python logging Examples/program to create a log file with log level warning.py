

import logging

logging.basicConfig(filename='log.txt', level=logging.WARNING)
# if file not exists-> it will create a new file
print("logging demo")
logging.critical("This is critical message")
logging.error("This is a error message")
logging.warning("This is warning message")

# set logging.DEBUG if you want all messages to write to log file
logging.info("This is info message")
logging.debug("This is debug message")

