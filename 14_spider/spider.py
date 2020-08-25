#! /usr/bin/env python

import requests
import re
import urlparse

target_url = "192.168.81.148/mutillidae/"
uniqe_list_link = []

def extract_links_from(url):
    response = requests.get("http://" + url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in uniqe_list_link:
            uniqe_list_link.append(link)
            print(link)
            crawl(url)


crawl(target_url)




