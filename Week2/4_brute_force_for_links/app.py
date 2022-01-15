#!/usr/bin/python3

import requests
from urllib.parse import urljoin

DOMAIN = 'https://prog-center.pro/'
ok_links = []
log_row = 'status: {} code: {} link: {}'


def txt2list(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text.split('\n')


def checkLink(link):
    result = requests.get(link)
    if result.status_code == 200:
        status = 'OK'
        ok_links.append(result.request.url)
    else:
        status = 'ERR'
    print(log_row.format(status, result.status_code, result.request.url))


def handelLinks():
    links = txt2list('links.txt')

    for i in range(len(links)):
        url = urljoin(DOMAIN, links[i])
        checkLink(url)


def showOkResult():
    print('ok results')
    for row in ok_links:
        print(row)


try:
    handelLinks()
    showOkResult()
except KeyboardInterrupt:
    print('[-] process stopped')
