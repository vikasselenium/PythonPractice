import logging

'''
By default, 
logging level: Warning
file mode: a
'''

#logging.basicConfig(filename='log.txt', level=logging.CRITICAL, filemode="w")
# logs with level WARNING and above (i.e., Warning, Error, Critical) are considered

logging.basicConfig() # sets up the root logger with default settings.
# if file not exists-> it will create a new file

logging.critical("This is critical message")
logging.error("This is a error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")
print("some print statement")

