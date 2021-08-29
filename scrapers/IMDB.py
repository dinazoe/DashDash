import requests
import json
from bs4 import BeautifulSoup

def get_api_key():
    file = open("api_key.txt", "r")
    key = file.read()
    file.close()
    return str(key)

api_key = get_api_key()

def get_movie_id(title, year="2021",tries=1):
    imdb_url = f"http://www.omdbapi.com/?apikey={api_key}&t={title.lower()}&y={year}"
    response = requests.get(imdb_url)
    json_data = json.loads(response.content)
    if 'imdbID' not in json_data:
        """
        if tries > 0:
            return get_movie_id(title, year="2020", tries=(tries - 1))
        else:
            return None
        """
        return None
    else:
        return json_data['imdbID']
    


def get_imdb_rating(title):
    
    id = get_movie_id(title)
    if id is None:
        ratings = {}
        ratings['metascore'] = "0"
        ratings['imdb'] = "0"
        return ratings
    
    url = f"https://www.imdb.com/title/{id}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='__next')
    elements = results.find_all(class_="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV")
    score_meta = results.find_all(class_="score-meta")
    ratings = {}
    ratings['metascore'] = "0"
    ratings['imdb'] = "0"

    for e in elements:
        ratings['imdb'] = e.text
    
    for e in score_meta:
        ratings['metascore'] = e.text
            
    return ratings