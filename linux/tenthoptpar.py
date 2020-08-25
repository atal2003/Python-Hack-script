#! /usr/bin/python3

from subprocess import Popen, PIPE
from email.mime.text import MIMEText
import smtplib

def report_via_email(message, recipient):
    msg = MIMEText(message)
    msg["Subject"] = "Low Disk Space Warning"
    msg["From"] = "atal"
    msg["TO"] = recipient 
    with smtplib.SMTP("smtp.gmail.com", port=587) as t:
        t.ehlo()
        t.starttls()
        t.login("darmal2017@gmail.com", "cheat123")
        t.sendmail("darmal2017@gmail.com", recipient, msg.as_string())

def report_via_stdout(message):
    print(message)

def check_once(options, partition_list):
    proc = Popen(["df", "-h"], stdout=PIPE)
    for line in proc.stdout:
        splitline = line.decode().split()
        for partition in partition_list:
            if splitline[5] == partition:
                percent = int(splitline[4][:-1])
                if percent > options.threshold:
                    message = "Warning: partition %s is %d%% full" % (partition, percent)
                    if options.mailbox:
                        #try:
                        report_via_email(message, options.mailbox)
                        #except Exception as e:
                           # print(e)
                    else:
                        report_via_stdout(message)


