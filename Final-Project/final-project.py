# Code Reference: https://realpython.com/python-send-email/

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "hanadulset0001@gmail.com"
password = "rahasia123123_"
    
def send_email(emailaddr):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Final Project Basic Python - Ika"
    message["From"] = sender_email
    message["To"] = emailaddr

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    You are receiving this email for Final Project Python from Indonesia.ai.
    This course is amazing, we learned so much throughout this month.
    You should join this course too if you want to start your career in Python"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, emailaddr, message.as_string()
        )

f = open("receiver-list.txt", "r")
for x in f:
  send_email(x)
  print("Sending email to", x)