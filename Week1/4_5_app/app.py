#!/usr/bin/python3

import os.path

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def addRow(string, result='result.txt'):
    if os.path.exists(result):
        fileMode = 'a'
    else:
        fileMode = 'w'
    with open(result, fileMode, encoding='utf-8') as f:
        f.write(string + '\n')


def search(author):
    browser.get('https://mdk-arbat.ru/')
    inputSelector = '.mdk-formsearch_input'
    bookSelector = '.tg-booktitle a'
    nextPageSelector = '.tg-pagination>ul>a'
    inputElem = browser.find_element_by_css_selector(inputSelector)
    inputElem.send_keys(author)
    inputElem.submit()
    i = 1
    while True:
        books_in_page = [
            elem.text for elem in browser.find_elements_by_css_selector(bookSelector)]
        for book in books_in_page:
            addRow(book)
        print('[+]' + f' books from {i} page processed')
        try:
            browser.find_element_by_css_selector(nextPageSelector).click()
        except Exception:
            break
        i += 1
    browser.close()


searchText = input('set the author you are looking for: ')
search(searchText)
