"""
Responsible for sending emails to myself.
Information will contain data scraped from YouTube via Selenium.
"""

import os
import smtplib
from datetime import date
from email.message import EmailMessage
from selenium_youtube_script import (
    latest_tracks,
    latest_tracks_links,
    popular_tracks,
    popular_tracks_links,
)

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASS = os.environ.get("GMAIL_PASS")
DATE = date.today().strftime("%B %d, %Y")

message = EmailMessage()
message["Subject"] = f"EDM Recommendations ({DATE})"
message["From"] = GMAIL_ADDRESS
message["To"] = GMAIL_ADDRESS
message.add_alternative(
    f"""\
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body style="font-family: 'Roboto', sans-serif;">
    <h1 style="color: #C2185B;">UPDATE THAT PLAYLIST!</h1>
    <p style="color: #C2185B;">Here are the latest and greatest songs from Future House Music! 🙌</p>
    <h2 style="color: #7B1FA2;">✨ LATEST TRACKS ✨</h2>
    <ul style="color: #7B1FA2;list-style-type: square;">
        <li><a href="{latest_tracks_links[0]}">{latest_tracks[0]}</a></li>
        <li><a href="{latest_tracks_links[1]}">{latest_tracks[1]}</a></li>
        <li><a href="{latest_tracks_links[2]}">{latest_tracks[2]}</a></li>
        <li><a href="{latest_tracks_links[3]}">{latest_tracks[3]}</a></li>
        <li><a href="{latest_tracks_links[4]}">{latest_tracks[4]}</a></li>
        <li><a href="{latest_tracks_links[5]}">{latest_tracks[5]}</a></li>
        <li><a href="{latest_tracks_links[6]}">{latest_tracks[6]}</a></li>
    </ul>
    <h2 style="color: #1976D2;">📈 POPULAR TRACKS 📈</h2>
    <ul style="color: #1976D2;list-style-type: square;">
        <li><a href="{popular_tracks_links[0]}">{popular_tracks[0]}</a></li>
        <li><a href="{popular_tracks_links[1]}">{popular_tracks[1]}</a></li>
        <li><a href="{popular_tracks_links[2]}">{popular_tracks[2]}</a></li>
    </ul>
    <hr>
    <p style="color: #00796B;"><em>"It's about time you fell in love with something that'll love you back and that, my friends, is house music! 😉"</em></p>
    <hr>
    <p>See you next week!</p>
</body>

</html>
""",
    subtype="html",
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(GMAIL_ADDRESS, GMAIL_PASS)
    smtp.send_message(message)
