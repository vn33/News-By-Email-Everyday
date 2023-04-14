import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vnaik7107@gmail.com"
    # password = os.getenv("PASSWORD")
    password = "qztbzvkjsnumewpg"

    receiver = "vnaik7107@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)