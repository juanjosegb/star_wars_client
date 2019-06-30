from django.contrib.sites import requests


def get_specie(url):
    r = requests.get(url)
    film = r.json()
    film_information = dict()
    film_information['name'] = film['title']
    film_information['classification'] = film['opening']
    film_information['designation'] = film['director']
    film_information['average_height'] = film['producer']
    film_information['skin_colors'] = film['release_date']
    film_information['hair_colors'] = film['characters']
    film_information['eye_colors'] = film['planets']
    film_information['average_lifespan'] = film['starships']
    film_information['homeworld'] = film['vehicles']
    film_information['people'] = film['species']
    film_information['films'] = film['films']
    return film_information
