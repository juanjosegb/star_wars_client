import requests


def get_film(pk):
    url = 'http://swapi.co/api/films/' + str(pk)
    r = requests.get(url)
    film = r.json()
    film_information = dict()
    film_information['title'] = film['title']
    film_information['opening'] = film['opening_crawl']
    film_information['director'] = film['director']
    film_information['producer'] = film['producer']
    film_information['release_date'] = film['release_date']
    film_information['characters'] = film['characters']
    film_information['planets'] = film['planets']
    film_information['starships'] = film['starships']
    film_information['vehicles'] = film['vehicles']
    film_information['species'] = film['species']
    return film_information
