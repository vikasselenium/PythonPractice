
import logging
import inspect

def get_custom_logger(loglevel):
    function_name=inspect.stack()[1][3]
    logger_name=function_name+" logger"

    logger = logging.getLogger(logger_name)
    logger.setLevel(loglevel) #dynamically setting loglevel i.e. coming from caller function

    filehandler=logging.FileHandler("application.log", mode="a")
    filehandler.setLevel(loglevel)

    formatter=logging.Formatter("%(asctime)s- %(levelname)s- %(name)s- %(message)s",
                                "%d/%m/%y %I:%M:%S %p")

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger

