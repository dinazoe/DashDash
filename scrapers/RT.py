"""
    Rotten tomatoes scraper
"""
from scrapers import IMDB as imdb
import requests
from bs4 import BeautifulSoup

class data_schema:
    def __init__(self, img_link, name, href, rt_rating, imdb, mc):
            self.img_link = img_link
            self.name = name
            self.href = href
            self.rt_rating = rt_rating
            self.imdb = imdb
            self.mc = mc


def get_front_page() -> str:
    base_url = "https://www.rottentomatoes.com"
    URL = 'https://www.rottentomatoes.com/browse/opening'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main-page-content')
    elements = results.find_all(class_="media-list__poster")
    rating_elements = results.find_all(class_="tMeterScore")
    out_list = []

    count = 0
    for e in elements:
        parent_href = e.parent.attrs['href']
        wtf = f"{base_url}{parent_href}"
        rt_rating = "None"
        if len(rating_elements) > count:
            rt_rating = str(rating_elements[count].next)
        attrs = e.attrs
        link = attrs['src']
        name = attrs['alt']
        imdb_rating = imdb.get_imdb_rating(name)
        out_list.append(data_schema(img_link=link, name=name, href=wtf, rt_rating=rt_rating, imdb=imdb_rating['imdb'], mc=imdb_rating['metascore']))
        count += 1
    
    return out_list


def get_rt_rating(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='topSection')
    elements = results.find_all(class_='tomatometer-container')
    for e in elements:
        for child in e:
            pass

data = get_front_page()
print(data)