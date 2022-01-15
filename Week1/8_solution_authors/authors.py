#!/usr/bin/python3

import json
from itertools import groupby
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = ChromeDriverManager().install()
browser = webdriver.Chrome(driver)
browser.get('https://quotes.toscrape.com/login')


def readAuthData():  # получение данных авторизации
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f).values()


def login(username, password):  # логин на страницу
    selector = '.form-control'
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'form'))
    )

    loginElem, pwdElem = element.find_elements_by_css_selector(selector)
    loginElem.send_keys(username)
    pwdElem.send_keys(password)
    pwdElem.submit()


def search():  # поиск авторов
    authorSelector = '.author'
    nextPageSelector = '.pager .next>a'
    author_list = []
    i = 1
    while True:
        author_in_page = [elem.text for elem in browser.find_elements_by_css_selector(
            authorSelector)]  # поиск автора на странице
        for tag in author_in_page:
            author_list.append(tag)  # добавление автора в список
        try:
            browser.find_element_by_css_selector(
                nextPageSelector).click()  # переход на следующую страницу
        except Exception:
            break
        i += 1
    author_list.sort()  # сортировка
    author_list = [el for el, _ in groupby(author_list)]  # удаление повторов
    with open('result.txt', 'w', encoding='utf-8') as f:  # запись в файл
        f.write(', '.join(author_list))
        f.close()
    browser.close()


login(*readAuthData())
search()
