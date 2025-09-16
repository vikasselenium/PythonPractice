import logging
#logging.exception(msg)

logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s",
                    datefmt="%d/%m/%Y %I/%M/%S %p")

logging.info("New Req")
try:
    x=int(input("Enter value for x: "))
    y=int(input("Enter value for y: "))

    res=x/y
    print(res)

except ZeroDivisionError as e:
    print(f"Zero division error- {e}")
    logging.exception(e)

except ValueError as e:
    print(f"Value error- {e}")
    logging.exception(e)

logging.info("Request process completed")
