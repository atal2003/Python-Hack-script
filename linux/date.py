#! /usr/bin/python3

from datetime import datetime

line = input("Enter your date of birth (DD/MM/YYYY): ")
birthday = datetime.strptime(line, "%d/%m/%Y")
print("you were born on a {0:%A}".format(birthday))



