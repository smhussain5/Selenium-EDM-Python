"""
Responsible for sending emails to myself.
Information will contain data scraped from YouTube via Selenium.
"""

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from selenium_youtube_script import (
    latest_tracks,
    latest_tracks_links,
    popular_tracks,
    popular_tracks_links,
)

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

<body>
    <h1>EDM RECOMMENDATIONS</h1>
    <h2>LATEST TRACKS</h2>
    <ul>
        <li><a href="{latest_tracks_links[0]}">{latest_tracks[0]}</a></li>
        <li><a href="{latest_tracks_links[1]}">{latest_tracks[1]}</a></li>
        <li><a href="{latest_tracks_links[2]}">{latest_tracks[2]}</a></li>
        <li><a href="{latest_tracks_links[3]}">{latest_tracks[3]}</a></li>
        <li><a href="{latest_tracks_links[4]}">{latest_tracks[4]}</a></li>
    </ul>
    <h2>POPULAR TRACKS</h2>
    <ul>
        <li><a href="{popular_tracks_links[0]}">{popular_tracks[0]}</a></li>
        <li><a href="{popular_tracks_links[1]}">{popular_tracks[1]}</a></li>
        <li><a href="{popular_tracks_links[2]}">{popular_tracks[2]}</a></li>
        <li><a href="{popular_tracks_links[3]}">{popular_tracks[3]}</a></li>
        <li><a href="{popular_tracks_links[4]}">{popular_tracks[4]}</a></li>
    </ul>
</body>

</html>
""",
    subtype="html",
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(GMAIL_ADDRESS, GMAIL_PASS)
    smtp.send_message(message)
