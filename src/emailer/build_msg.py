from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from flask import render_template

def build_mime_multipart_message(email_address:str, to, subject:str, template:str, context: dict) -> MIMEMultipart:
  if isinstance(to, str):
      to = [to]
  
  to_str = ""
  for recipient in to:
      to_str += (f"{recipient},")

  msg = MIMEMultipart('related')
  msg['Subject'] = subject
  msg['From'] = email_address
  msg['To'] = to_str
  msg.preamble = 'This is a multi-part message in MIME format.'

  msgHTML = MIMEText(render_template(template, **context), 'html')
  msg.attach(msgHTML)

  # adds images stored in image registry for the current template to
  # the MIME message
  # for entry in image_registry[template]:
  #   with open(entry.img_path, 'rb') as img_file:
  #     msgImage = MIMEImage(img_file.read())
  #     msgImage.add_header('Content-ID', f"<{entry.cid}>")
  #     msg.attach(msgImage)

  return msg