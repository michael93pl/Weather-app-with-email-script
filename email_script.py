import smtplib
import additional
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import main

server_info = smtplib.SMTP('smtp.gmail.com', 587)



def sending_email():
    """Email script with email box input from user)"""

    reciever_addr = input("Please provide Your email adress\n")
    time = datetime.datetime.now()
    #server commends
    server = server_info
    server.ehlo()
    server.starttls()
    server.ehlo()


    #credentials of sender
    who = "michael93pl"
    password = additional.x


    #logging in
    server.login(who, password)

    #template for recievers
    toaddr = [reciever_addr]
    cc = []
    subject = "Weather for {}.".format(time)
    text = str(main.send())

    #MSG template


    message = MIMEMultipart()
    message['From'] = "Michal <{}>".format(who)
    message['To'] = ", ".join(toaddr)
    message['Cc'] = ", ".join(cc)
    message['Subject'] = subject
    message.attach(MIMEText(text))

    msg = message.as_string()

    #Join reciever with CC

    final_to = cc + toaddr



    server.sendmail(who, final_to, msg)


    print("Email sent at {}".format(time))

