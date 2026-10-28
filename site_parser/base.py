import requests

from bs4 import BeautifulSoup

print('base')

class BaseParser:
    URL = 'https://upl.uz'

    def get_soup(self, url=URL):
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
