#use both console and file handler

import logging

logger=logging.getLogger("demo_logger")
logger.setLevel(logging.DEBUG)

# StreamHandler -> for printing logs on console
# FileHandler   -> for writing logs in a file

console_handler=logging.StreamHandler()
file_handler=logging.FileHandler("Both_logs.txt", mode="w")

# Formatter for both handlers
formatter1=logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s",
                            "%d/%m/%Y %I:%M:%S %p")
formatter2=logging.Formatter("%(levelname)s %(name)s %(message)s")

#setting formatter for both handlers
console_handler.setFormatter(formatter2)
console_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter1)
file_handler.setLevel(logging.DEBUG)

#adding handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#using custom logger
logger.critical("This is critical message")
logger.error("This is error message")
logger.warning("This is warning message")
logger.info("This is info message")
logger.debug("This is debug message")