import logging

logger = logging.getLogger("ecommerce_app")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

file_handler = logging.FileHandler("log-files/app.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Debug message")
logger.info("Server started successfully")
logger.warning("Low inventory for product ID 101")
logger.error("Payment gateway timeout")
logger.critical("Database connection lost")

