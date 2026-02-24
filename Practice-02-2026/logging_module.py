import logging

logging.basicConfig(filename="log-files/example.log", level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

logging.debug("This is a Debug message")
logging.info("This is a Message message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")