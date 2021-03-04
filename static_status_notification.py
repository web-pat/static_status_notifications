import json
import smtplib

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# E-mail properties    
def send_email(data):
    email = 'youremailaddress'
    password = 'yourpassword'
    send_to_email = 'sendtoaddress'
    subject = 'Notification: service offline'
    message = 'One or several of your services are currently offline: ' + data_string
    
    msg = MIMEMultipart()
    msg ['From'] = email
    msg ['To'] = send_to_email
    msg ['Subject'] = subject
    
    #Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('your.smtp.server', 587) #Insert your own smtp-server credentials
    server.starttls()
    server.login(email, password)
    text = msg.as_string() #Convert the MIMEMultipart object to a string to send
    server.sendmail(email, send_to_email, text)
    server.quit()

# Import json data. If file resides in different location, enter full path for status.json
with open('status.json', 'r') as status:
    data = json.load(status)

# Check for outages, convert to string and send mail
for outage in data:
    if outage['status'] == 'Fail':
        data_string = json.dumps(outage)
        send_email(data)
