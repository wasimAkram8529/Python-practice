import logging
import logging.handlers
from dotenv import load_dotenv
import os
# import smtplib

load_dotenv()


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# setup host datails
smtp_server = os.getenv('SMTP_SERVER')
port = int(os.getenv('SMTP_PORT')) # for TLS

# set up user detail
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
recipient = os.getenv('RECIPIENT')

# create formatter
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

# create SMTP Handlers
smtp_handler = logging.handlers.SMTPHandler(
  mailhost=(smtp_server, port),
  fromaddr=username,
  toaddrs=[recipient],
  subject='Critical Error Alert',
  credentials=(username, password),
  secure=(),
  timeout=10
)

smtp_handler.setLevel(logging.CRITICAL)
smtp_handler.setFormatter(formatter)

logger.addHandler(smtp_handler)

try:
  raise ValueError('A critical error occured')
except ValueError as v:
  logger.critical(f"ValueError: {v}", exc_info=True)


