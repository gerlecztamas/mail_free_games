import os
import smtplib, ssl
from email.message import EmailMessage

from giveaway import Giveaway

def send_email(body):
    email_from = os.environ.get("EPIC_EMAIL_USER_FROM")
    password = os.environ.get("EPIC_EMAIL_PASS")
    email_to = os.environ.get("EPIC_EMAIL_USER_TO")

    if not email_from or not password or not email_to:
        raise RuntimeError("Email credentials not set in environment variables!")
    
    msg = EmailMessage()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = "Today's new free games on Epic Store!"
    msg.set_content(body)

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_from, password)
            server.send_message(msg)


def convert_games_to_mail_body(games: list[Giveaway]) -> str:
    lines = []
    
    for game in games:
        lines.append(f"{game.title}\n{game.open_giveaway_url}\nEnds at: {game.end_date}")

    return "\n".join(lines)