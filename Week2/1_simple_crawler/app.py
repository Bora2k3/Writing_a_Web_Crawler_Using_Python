#!/usr/bin/python3
# краулер для считывания всех внутренних ссылок сайта
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)
domain = 'https://prog-center.pro'
urls_to_visit = [domain] # список ссылок сайта
visited_urls = [] # список посещенных ссылок

def check_link(path):
    return (path.startswith(domain) or path.startswith('/'))

def extract_links(links_list): # очистка списка ссылок

    for link in links_list:
        path = link.get('href')
        if path is None:
            continue
        if check_link(path):
            new_url = urljoin(domain, path)
            if new_url in urls_to_visit:
                continue
            urls_to_visit.append(new_url)

def get_linked_urls(url): # парсер ссылок
    message = f'{url} visited urls: {len(visited_urls)} urls to visit: {len(urls_to_visit)}'
    logging.info(f'Crawling: {message}')

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    links_list = soup.find_all('a')
    extract_links(links_list)
    visited_urls.append(url)

for link in urls_to_visit:
    get_linked_urls(link)

with open('urls_to_visit.txt', 'w') as f:
    f.write('\n'.join(urls_to_visit))

with open('visited_urls.txt', 'w') as f:
    f.write('\n'.join(visited_urls))


