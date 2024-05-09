"""
Responsible for sending emails to myself.
Information will contain data scraped from YouTube via Selenium.
"""

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASS = os.environ.get("GMAIL_PASS")

message = EmailMessage()
message["Subject"] = "SUBJECT HERE"
message["From"] = GMAIL_ADDRESS
message["To"] = GMAIL_ADDRESS
message.add_alternative(
    f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="color:SlateGray;">
    <p style="font-weight:bold;">{GMAIL_PASS}</p>
</body>
</html>
""",
    subtype="html",
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(GMAIL_ADDRESS, GMAIL_PASS)
    smtp.send_message(message)
