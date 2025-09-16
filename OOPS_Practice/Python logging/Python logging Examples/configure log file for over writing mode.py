
import logging

logging.basicConfig(filename="log.txt", level=logging.CRITICAL, filemode="w")
# logging.basicConfig()
# file modes: a,w
# default level= Warning(30)
# filename-> if no filename then logs will be printed to console

logging.critical("This is critical message")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")