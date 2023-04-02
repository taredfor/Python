import time

import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.kinopoisk.ru/lists/movies/top250/'

def response_func(url):
    driver = webdriver.Chrome()
    result = driver.get(url)
    time.sleep(60)
    elements = driver.find_elements(By.CSS_SELECTOR, "span[class='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj']")
    return elements


for elem in response_func(url):
    print(""" elem.text """)





