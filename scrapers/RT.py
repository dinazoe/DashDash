"""
    Rotten tomatoes scraper
"""

import requests
from bs4 import BeautifulSoup

class data_schema:    
    def __init__(self, img_link, name):
            self.img_link = img_link
            self.name = name


def get_front_page() -> str:    
    URL = 'https://www.rottentomatoes.com/browse/opening'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main-page-content')
    elements = results.find_all(class_="media-list__poster")
    

    out_list = []

    for e in elements:
        attrs = e.attrs
        link = attrs['src']
        name = attrs['alt']
        out_list.append(data_schema(img_link=link, name=name))


    return out_list

data = get_front_page()
print(data)