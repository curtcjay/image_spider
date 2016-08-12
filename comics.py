import requests
from bs4 import BeautifulSoup
import urllib.request
import os

page = 176
max_pages = 200
all_links = []

while page <= max_pages:
    url = "http://www.viewcomic.com/page/" + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        href = link.get('href')
        all_links.append(href)
    page += 1

all_links = list(set(all_links))
f = open("comic_links_p6.txt", "w")
f.write("\n".join(str(x) for x in all_links))
f.close()
