import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
port = int(os.getenv('SMTP_PORT')) # for TLS
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
recipient = os.getenv('RECIPIENT')

# Simple email structure
# from_address = os.getenv('SMTP_SERVER')
# to_address = os.getenv('RECIPIENT')
# message = "Subject: Test email\n\n This is a test email message"

# server.sendmail(from_address, to_address, message)
# print("Email sent successfully.")

# Setup complex email structure
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = recipient
msg['Subject'] = "Test Email"

text_content = 'This is a test email message'
html_content = '''<!DOCTYPE html>
<html>
<body>
  <h1>This an HTML Email</h1>
  <p>This is test email message</p>
</body>
</html>
'''
# msg.attach(MIMEText(text_content, 'plain'))
msg.attach(MIMEText(html_content, 'html'))

email_message = msg.as_string()

server = smtplib.SMTP(smtp_server, port)
server.starttls()
print("Secure connection started.")
server.login(username, password)
print("Authentication done successfully.")

print(f"Email message: {email_message}")
server.sendmail(msg['From'], msg['To'], email_message)
print("Email sent successfully.")


server.close()

