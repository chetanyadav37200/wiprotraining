"""

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser=input('What browser you want to use')
match browser.lower():
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resource/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resource/msedgedriver.exe'))
    case _:  # default
        driver = webdriver.Edge(service=Service('../resource/msedgedriver.exe'))

driver.get('https://www.google.com')

pagetitle=driver.title

if pagetitle=='Google':
    print('Google page is loaded')
else:

    print('Google page is not loaded')
sleep(6)
driver.quit()