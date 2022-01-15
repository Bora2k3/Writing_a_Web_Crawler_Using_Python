#!/usr/bin/python3

import json
import time
import requests
import urllib.parse

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = ChromeDriverManager().install()
browser = webdriver.Chrome(driver)
browser.get('https://www.instagram.com/')

loaded_photos = []


def readAuthData():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f).values()


def login(mail, pwd):
    selector = '._2hvTZ'
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'form'))
    )

    loginElem, pwdElem = element.find_elements_by_css_selector(selector)
    loginElem.send_keys(mail)
    pwdElem.send_keys(pwd)
    pwdElem.submit()


def search(value):
    inputSelector = '.XTCLo'
    inputElem = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, inputSelector))
    )
    inputElem.send_keys(value)
    target = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.fuqBx div a'))
    )
    target.click()


def scrollBottom():
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.EZdmt'))
    )
    SCROLL_PAUSE_TIME = 2
    page_num = 1
    while True:
        getPhotos(page_num)
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        page_num += 1


def getPhotos(page_num):
    photoSelector = '.FFVAD'
    photos = browser.find_elements_by_css_selector(photoSelector)
    index = 1
    for photo in photos:
        photo_link = photo.get_attribute('src')
        savePhoto(f'{page_num}_{index}.jpeg', photo_link)
        index += 1


def savePhoto(photo_name, url, folder='result/'):
    if url in loaded_photos:
        return
    loaded_photos.append(url)
    file = requests.get(url)
    filePath = urllib.parse.urljoin(folder, photo_name)
    with open(filePath, '+wb') as f:
        f.write(file.content)


login(*readAuthData())
search('#bike')
try:
    scrollBottom()
    time.sleep(10)
    browser.close()
except KeyboardInterrupt:
    print('[-] process stopped')
