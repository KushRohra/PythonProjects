import smtplib
from email.mime.text import MIMEText


def send_email(email, height, avg_height, count):
    from_email = "youremail@email.com"
    from_password = "yourpassword"
    to_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s</strong> cm" % height
    message += "<br>Avg height of all the people is <strong>%s</strong> cm" % avg_height
    message += "<br><strong>%s</strong> people helped us in doing this survey" % count

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('64.233.184.108', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
