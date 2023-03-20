import requests
from bs4 import BeautifulSoup

def get_article_tag(page_id:int):
    if page_id < 1 or page_id > 1:
        raise ValueError('page_id < 1 or page_id > 1')
    url = f'https://stackoverflow.com/questions/tagged/python?tab=newest&page={page_id}&pagesize=15'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    param = {'class': 's-link'}
    search_result = soup.find_all('a', param)
    result = []
    for i in search_result:
        result.append(i.text)
    for i in range(0, 2):
        result.remove('\n\n')
        if i == 1:
            result.pop()
    return result


def take_result(page_id: int):
    l_ist = get_article_tag(page_id)
    for i in l_ist:
        print('"', i, '"')
    return


print(take_result(1))