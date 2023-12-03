import os
import smtplib
from email.message import EmailMessage
import datetime

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"  # Adjust server address, if you are not using @outlook

# Load the environment variables
sender_email = "abc1@gmail.com"  # Replace with your sender email
password_email = "234"  # Replace with your email password

def send_email(subject, receiver_email, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(message)
    
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    recipient_email = "qwe@gmail.com"
    message = "Hello, this person is interested in buying a property.\nCustomer Email: erw@gmail.com"

    send_email(
        subject="Property Inquiry",
        receiver_email=recipient_email,
        message=message
    )
