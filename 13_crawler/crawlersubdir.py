#! /usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = "192.168.81.148/multillidae"

try:
    with open("/root/Downloads/sub_list", "r") as sub:
        for line in sub:
            word = line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print("Discovered subdirectory  ....> " + test_url)
except requests.exceptions.InvalidURL:
 pass
