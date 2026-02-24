import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
port = int(os.getenv('SMTP_PORT')) # for TLS
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
recipient = os.getenv('RECIPIENT')
recipient2 = os.getenv('RECIPIENT2')

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
log_file_name = "app.log"

log_file_location = os.path.join(parent_dir, log_file_name)

def send_email(subject, body,log_file_path):
  sender_email = username
  receiver_email = recipient2
  #receiver_email = recipient
  password = password

  msg = MIMEMultipart(body)
  msg["subject"] = subject
  msg["from"] = sender_email
  msg["to"] = receiver_email

  msg.attach(MIMEText(body, 'plain'))

  with open(log_file_path, "rb") as attachment:
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())

  encoders.encode_base64(part)
  part.add_header(
      "Content-Disposition",
      f"attachment; filename={log_file_path.split('/')[-1]}",
  )

  msg.attach(part)

  try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls() 
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Email sent successfully")
  except Exception as e:
      print(f"Error: {e}")
  finally:
      server.quit()


send_email("Backup completed", "Backup created successfully", log_file_location)  