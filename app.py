import smtplib
import additional
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#server commends
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()


#credentials of sender
FROM = "michael93pl"
PASSWORD = additional.x


#logging in
server.login(FROM, PASSWORD)

#template for recievers
TOADDR = ["michael93pl@gmail.com"]
CC = []
SUBJECT = "testing"
TEXT = "TEST FOR GITHUB"

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

TIME = datetime.datetime.now()
print("Email sent at {}".format(TIME))

