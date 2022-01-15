from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = ChromeDriverManager().install()
browser = webdriver.Chrome(driver)
browser.get('https://google.com')
inputSelector = '.gLFyf.gsfi'
inputElem = browser.find_element_by_css_selector(inputSelector)
inputElem.send_keys('planetary hub bike')