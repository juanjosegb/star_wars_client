from django.contrib.sites import requests


def get_all_film_names():
    url = 'http://swapi.co/api/films'
    r = requests.get(url)
    films = r.json()
    film_list = films['results']
    film_names = []
    for film in film_list:
        film_names.append(film['title'])
    return film_names
