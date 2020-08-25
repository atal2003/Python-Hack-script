#! /usr/bin/python3
username = input("Login: >>")


user_list = ["atal", "aimal", "qais", "adrees"]
user_list.append("zoelay")

#control that the user belongs to the list of allowed users
if username in user_list: 
    print ("Access granted")
else:
    print ("Access denied")
