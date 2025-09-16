
import logging
import inspect

def customlogger(loglevel=logging.DEBUG):
    #logger=logging.getLogger(__file__)
    logger = logging.getLogger(inspect.stack()[1][3])
    logger.setLevel(loglevel)

    filehandler=logging.FileHandler("automation.log")
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger
