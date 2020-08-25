#! /usr/bin/python3

from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

def email_test(subject, recipient):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = "atal"
    msg["To"] = recipient
    msg.attach(MIMEText("Body"))
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
    #the security for gmail need to be disable so then the user and password works. 
        smtp.login("darmal2017@gmail.com", "cheat123")
        smtp.send_message(msg)
        print("sent...")

email_test("test", "darmal2017@gmail.com")


    
