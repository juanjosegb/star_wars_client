from django.contrib.sites import requests


def get_planet(url):
    r = requests.get(url)
    planet = r.json()
    planet_information = dict()
    planet_information['name'] = planet['name']
    planet_information['rotation_period'] = planet['rotation_period']
    planet_information['orbital_period'] = planet['orbital_period']
    planet_information['diameter'] = planet['diameter']
    planet_information['climate'] = planet['climate']
    planet_information['gravity'] = planet['gravity']
    planet_information['terrain'] = planet['terrain']
    planet_information['surface_water'] = planet['surface_water']
    planet_information['population'] = planet['population']
    planet_information['residents'] = planet['residents']
    planet_information['films'] = planet['films']
    return planet_information
