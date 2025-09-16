import logging

# logging.basicConfig(format="%(asctime)s: %(levelname)s : %(message)s",
#                     datefmt='%d/%m/%Y  %I:%M:%S %p')

logging.basicConfig(format="%(asctime)s: %(levelname)s : %(message)s",
                    datefmt='%d/%m/%Y  %H:%M:%S')

# %I = 12 hours scale
# %H = 24 hours scale

print("logging demo")
logging.critical("This is a critical message")
logging.error("This is a error message")
logging.warning("This is a warning message")
logging.info("This is a info message")
logging.debug("This is a debug message")