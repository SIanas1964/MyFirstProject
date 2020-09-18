#!/usr/bin/env python3
"""
Generate email
"""
from email.message import EmailMessage
import mimetypes
import smtplib
import os.path

def generate_email(sender, recipient, subject, body, attachement_path=None):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    if attachement_path != None:
        attachement_filename = os.path.basename(attachement_path)
        mime_type, _ = mimetypes.guess_type(attachement_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachement_path, 'rb') as file:
            message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=attachement_filename)
        
    return message

def send_email(message):
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()
