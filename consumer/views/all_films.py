from django.contrib.sites import requests


def get_all_film_names():
    url = 'http://swapi.co/api/films'
    r = requests.get(url)
    films = r.json()
    film_list = films['results']
    film_names = dict()
    for film in film_list:
        film_names[film['title']] = film['url']
    return film_names
