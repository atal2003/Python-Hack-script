#! /usr/bin/python3
# time module
#time.time()      show secondd from 1970 used for calcuation
#datetime module :   datetime.strptime is sring  example dt = datetime.striptime("2020/01/01", "%Y/%m/#d") we will tell what to to be very usefull Mosh tutorial. 
# to conver time.time() to datetime we use datetime.fromtimestamp(time.time()) will change it. 
# datetime object has month and year attribule like dt = datetime.now()  dt.mont  dt.year  
# dt.strftime is oposite of strptime it convert string to datetime object. 


from datetime import datetime, timedelta
import os
#st_mtime is seconds
# %B month example January
# %Y  2020
# 

rootinfo = os.stat("/")
rootmodtime = datetime.fromtimestamp(rootinfo.st_mtime)
print(rootmodtime)


rightnow = datetime.now()
print(rightnow)



since = rightnow - rootmodtime

print("'/' was modified {} days, {} hours and {} minutes ago".format(
            since.days, 
            since.seconds//3600, 
            (since.seconds%3600)//60))


fortnight = timedelta(days=14)
dueback = rightnow + fortnight

print("your book is due back on {0:%d} of {0:%B}".format(dueback))


