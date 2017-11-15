import smtplib
import additional
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import main

def sending_email():
    """Email script with email box input from user)"""

    EMAIL_BOX = input("Please provide Your email adress\n")
    TIME = datetime.datetime.now()
    #server commends
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    #credentials of sender
    FROM = "xxx"
    PASSWORD = additional.x


    #logging in
    server.login(FROM, PASSWORD)

    #template for recievers
    TOADDR = [EMAIL_BOX]
    CC = []
    SUBJECT = "Weather for {}.".format(TIME)
    TEXT = str(main.send())

    #MSG template


    message = MIMEMultipart()
    message['From'] = "Michal <{}>".format(FROM)
    message['To'] = ", ".join(TOADDR)
    message['Cc'] = ", ".join(CC)
    message['Subject'] = SUBJECT
    message.attach(MIMEText(TEXT))

    MSG = message.as_string()

    #Join reciever with CC

    FINAL_TO = CC + TOADDR



    server.sendmail(FROM, FINAL_TO, MSG)


    print("Email sent at {}".format(TIME))

