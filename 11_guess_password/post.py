#! /usr/bin/evn python


import requests


target_url = "http://192.168.81.148/dvwa/login.php"

data_dict = {"Name": "atal", "Password": "password", "Login" : "submit"}

response = requests.post(target_url, data=data_dict)

response2 = requests.get(target_url)
print(response.content)






