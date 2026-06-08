from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_password(receiver_email, password):

    msg = EmailMessage()
    msg["Subject"] = "VendorApp Password Recovery"
    msg["From"] = EMAIL_USER
    msg["To"] = receiver_email

    msg.set_content(
        f"Your password is: {password}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)