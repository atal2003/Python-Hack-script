#! /usr/bin/python3

from datetime import datetime, timedelta
from time import sleep # just to pause between to exectuion of code 

dt1 = datetime(2019, 1, 1)
dt2 = datetime.now()

duration = dt2 -dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())

sleep(3)

#total_seconds is function. 

dt1 = datetime(2019, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()

duration = dt2 -dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())
