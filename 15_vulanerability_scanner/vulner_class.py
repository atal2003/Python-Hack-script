#! /usr/bin/env python

import scanner_vulneral


target_url = "http://192.168.81.148/mutillidae/index.php?page=login.php"
#data_dict = {"username": "admin", "Password": "password", "Login": "submit"}

vulneral = scanner_vulneral.Scanner(target_url)
#vulneral.session.post("http://192.168.81.148/dvwa/login.php", data=data_dict)

a = vulneral.extract_forms(target_url)
print(a)

