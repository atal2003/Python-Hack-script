#! /usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = raw_input("enter your target url >  ")

try:
    with open("/root/Downloads/sub_list", "r") as sub:
        for line in sub:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                print("fine the subdomain  ....> " + test_url)
except requests.exceptions.InvalidURL:
 pass






