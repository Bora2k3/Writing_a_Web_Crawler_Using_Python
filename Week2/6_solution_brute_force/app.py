#!/usr/bin/python3

import requests
from urllib.parse import urljoin

DOMAIN = 'https://books.toscrape.com/'
ok_links = []
log_row = 'status: {} code: {} link: {}'


def txt2list(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text.split('\n')


def checkLink(link):
    result = requests.get(link)
    if result.status_code == 403:
        ok_links.append(result.request.url)


def handelLinks():
    links = txt2list('links.txt')

    for i in range(len(links)):
        url = urljoin(DOMAIN, links[i])
        checkLink(url)


def writeFile():
    ok_links.sort()
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(ok_links))
        f.close()


try:
    handelLinks()
    writeFile()
except KeyboardInterrupt:
    print('[-] process stopped')
