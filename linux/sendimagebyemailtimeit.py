#! /usr/bin/python3

from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from timeit import timeit

code1 = """
msg = MIMEMultipart()
msg["Subject"] = "Low Disk Space Warning"
msg["From"] = "asafiatal@gmail.com"
msg["TO"] = "ashansafi@yahoo.com"
msg.attach(MIMEImage(Path("/mnt/c/Users/ashan/Desktop/me.JPG").read_bytes()))


with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("asafiatal@gmail.com", "Nabi@1971")
    smtp.send_message(msg)
 """
print(timeit(code1, number=10)

