from bs4 import BeautifulSoup
import requests
from numpy.core.defchararray import lstrip

url = 'https://dtf.ru/'
response = requests.get(url)
# print(type(response))
soup = BeautifulSoup(response.text, 'html.parser')

def get_articale_name(url):
    global st_r
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    attr = {'class': 'content-title'}
    try:
        st_r = soup.find('h1', attr).text
    except Exception:
        st_r = soup.find('p').text
    return lstrip(st_r)


# print(get_articale_name('https://dtf.ru/s/713649-neyrobaza'))

def get_articale_date(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    attr = {'class': 'time'}
    st_r = soup.find('time', attr)['title']
    return st_r


# print(get_article_date(url))

def get_articale(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    attr = {'class': 'content-link'}
    st_r = soup.find_all('a', attr)
    for i in st_r:
        url_list = i['href']
        print(url_list)
        print(f'{get_articale_name(url_list)} | {get_articale_date(url_list)}')


print(get_articale(url))
