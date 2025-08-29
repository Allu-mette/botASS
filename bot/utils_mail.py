import smtplib
from email.mime.text import MIMEText

from config import BOT_MAIL, BOT_MAIL_PASSWD, TARGET_MAIL

SENDER = BOT_MAIL
PASSWD = BOT_MAIL_PASSWD
RECIPIENT = TARGET_MAIL

def sendMail(content: str):

        # Create the MIME message
    message = MIMEText(content, 'html')
    message['From'] = SENDER
    message['To'] = RECIPIENT
    message['Subject'] = "Exo du jour"

        # Send the message on google smtp server (gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() 
        server.login(SENDER, PASSWD)
        server.send_message(message)