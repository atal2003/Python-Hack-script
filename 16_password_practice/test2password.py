#! /usr/bin/env python


password_to_check = 3879
with open("/usr/share/wordlists/rockyou.txt", "rb") as file_name:
    file_name.read()
    for line in file_name:
        if line == password_to_check:
            print("password found")
        else:
             print("no much found")
