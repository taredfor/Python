import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.goodreads.com/list/show/7.Best_Books_of_the_21st_Century"

def response_func(url):
      driver = webdriver.Chrome()
      result = driver.get(url)
      time.sleep(60)
      nums = driver.find_elements(By.CSS_SELECTOR, "td[class='number']")
      elements = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='name']")
      return elements


j = 0
for i in response_func(url):
      if i.text != "J.K. Rowling":
            j += 1
            print(j, i.text)

