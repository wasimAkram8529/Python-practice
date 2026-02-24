import logging

logging.basicConfig(
  filename="log-files/login.log", 
  level=logging.INFO, 
  format='%(asctime)s | %(levelname)s | %(message)s'
)

def user_logging(username, password):
  try:
    if username == "admin" and password == "1234":
      logging.info(f"User {username} logged in successfully")
      return True
    else:
      logging.warning(f"Failed login attempt for user {username}")
      return False
  except Exception as e:
    logging.error(f"Login error: {str(e)}")

user_logging("admin", "1234")
user_logging("user", "5678")