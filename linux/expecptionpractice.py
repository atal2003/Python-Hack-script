#! /usr/bin/python3

from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path

msg = MIMEMultipart()
msg["Subject"] = "Low Disk Space Warning"
msg["From"] = "darmal2017@gmail.com"
msg["TO"] = "ashansafi@yahoo.com"
msg.attach(MIMEImage(Path("/mnt/c/Users/ashan/Desktop/me.JPG").read_bytes()))

try:
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("darmal2017@gmail.com", "123")
        smtp.send_message(msg)
except smtplib.SMTPAuthenticationError as ex:
    print(ex)

print("well done ATAL")
##def report_via_stdout(message):
##    print(message)
##
##def check_once(options, partition_list):
##    proc = Popen(["df", "-h"], stdout=PIPE)
#    for line in proc.stdout:
#        splitline = line.decode().split()
#        for partition in partition_list:
#            if splitline[5] == partition:
#                percent = int(splitline[4][:-1])
#                if percent > options.threshold:
#                    message = "Warning: partition %s is %d%% full" % (partition, percent)
#                    if options.mailbox:
#                        try:
#                            report_via_email(message, option.mailbox)
#                        except Exception as e:
#                            print(e)
#                    else:
#                        report_via_stdout(message)
#
#
