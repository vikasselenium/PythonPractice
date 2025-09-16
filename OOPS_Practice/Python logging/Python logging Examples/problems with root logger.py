
# if we make configuration for root logger then those are fina;
# we will not able to make changes on that later on
# we can use file handler or console handler at a time but not both simultaneously
# all data is logged in single file log can be collected per module/class/methods
# it is not possible tp configure logger with different configurations at same time

import logging
import log_test

#logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    filemode="a", format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
                    datefmt="%d/%m/%Y -%I:%M:%S %p")

logging.critical("This is aa critical message")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")

