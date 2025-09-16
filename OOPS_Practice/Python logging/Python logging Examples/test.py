import logging
import student

logger=logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)

filehandler=logging.FileHandler("test_log.txt")
filehandler.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                            "%d/%m/%Y %I:%M:%S %p")

filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

logger.critical("This is critical message")
logger.error("This is error message")
logger.warning("This is warning message")
logger.debug("This is debug message")

