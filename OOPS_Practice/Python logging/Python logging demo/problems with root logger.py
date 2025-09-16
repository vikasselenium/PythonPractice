import logging
'''
there are few problems with root logger
- once initialized/configured we will not able to configure it
- we will not able to print logs at console and in file at once
'''


logging.basicConfig(level=logging.DEBUG) # we can use int value here also

logging.basicConfig(filename="log_123.txt", level=logging.ERROR,
                    filemode="a", format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
                    datefmt="%d/%m/%Y -%I:%M:%S %p")




logging.critical("This is aa critical message")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")