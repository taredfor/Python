import requests


# https://api.spaceflightnewsapi.net/v4/articles/

def get_inform(i):
    url = f'https://api.spaceflightnewsapi.net/v4/articles/{i}/'
    result = requests.get(url).json()
    return result['id'], result['title'], result['url']


for i in range(1, 11):
   print(get_inform(i))

# https://ulvis.net/developer.html


your_long_url = 'https://github.com/lamerman/shellpy'
your_custom_name = 'apple123'


def short_url(your_long_url: str, your_custom_name: str):
    url = f'https://ulvis.net/api.php?url={your_long_url}&custom={your_custom_name}&private=1'
    result = requests.get(url)
    return result.text
