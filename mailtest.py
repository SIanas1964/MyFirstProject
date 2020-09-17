from email.message import EmailMessage
import mimetypes
import smtplib
message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """ Hi there!
I'm learning to send emails using Python!"""
message.set_content(body)

mime_type, _ = mimetypes.guess_type("example.png")
mime_type, mime_subtype = mime_type.split('/', 1)

print(mime_type, mime_subtype)

with open("example.png", 'rb') as file:
    message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename="example.png")

mail_server = smtplib.SMTP('localhost')