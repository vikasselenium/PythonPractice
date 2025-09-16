
'''
we need to create 3 objects
 - logger object
 - Handler object = streamhandler=> console, file=>file handler, smtphandler=email
                    httphandler=> web server
 - formatter object:
      - to format log message e.g. date and time
      1. create logger object and set level
         logger=logging.getlogger('demologger')
         logger.setlevel(logging.DEBUG)

     2. create handler object and set level
         consoleHandler=logging.StreamHandler()
         consoleHandler.setlevel(logging.ERROR)

         fileHandler=logging.FileHandler('abc.log',mode="w")
         filehandler.setlevel(logging.ERROR)

    3. create formatter object
       formatter=logging.Formater('%(asctime)s:%(levelname)s':%(name)s:%(message)s,
                                 datefmt="%d/%m/%Y %I/%M/%s %p')

    4. set formatter to handler
    controlhandler.setFormatter(formatter)

    5. Add handler to logger
       logger.addhandler(consolehandler)

    6. write log messages by logger object
    logger.critical()
    logger.error()
    logger.warning()
    logger.info()
    logger.debug()

    



'''
