import requests
from bs4 import BeautifulSoup


# request to url
def request(url,headers):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
