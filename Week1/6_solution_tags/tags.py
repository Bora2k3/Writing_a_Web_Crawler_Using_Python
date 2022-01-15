#!/usr/bin/python3
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = ChromeDriverManager().install()
browser = webdriver.Chrome(driver)


def search():
    browser.get('https://quotes.toscrape.com/js-delayed')
    time.sleep(11)
    tagSelector = '.tag'
    tags_in_page = [
        elem.text for elem in browser.find_elements_by_css_selector(tagSelector)]
    tag_list = []
    for tag in tags_in_page:
        tag_list.append(tag)
    tag_list.sort()
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(', '.join(tag_list))
        f.close()
    browser.close()


search()
