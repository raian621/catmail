from smtplib import SMTP_SSL
from .build_msg import build_mime_multipart_message

class Emailer:

  def __init__(self, email_address, email_password, smtp_address, smtp_port):
    self.email_address = email_address
    self.email_password = email_password
    self.smtp_server = SMTP_SSL(
      host=smtp_address,
      port=smtp_port
    )

    self.smtp_server.login(email_address, email_password)
  
  def __del__(self):
    if (self.smtp_server):
      self.smtp_server.close()

  def send_email(self, template, to, subject, context):
    msg = build_mime_multipart_message(self.email_address, to, subject, template, context)     
    self.smtp_server.send_message(msg)