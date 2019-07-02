import requests


def get_character(pk):
    url = 'http://swapi.co/api/people/' + str(pk)
    r = requests.get(url)
    character = r.json()
    character_information = dict()
    character_information['name'] = character['name']
    character_information['height'] = character['height']
    character_information['mass'] = character['mass']
    character_information['hair_color'] = character['hair_color']
    character_information['skin_color'] = character['skin_color']
    character_information['birth_year'] = character['birth_year']
    character_information['gender'] = character['gender']
    character_information['homeworld'] = character['homeworld']
    character_information['films'] = character['films']
    character_information['starships'] = character['starships']
    character_information['vehicles'] = character['vehicles']
    character_information['species'] = character['species']
    return character_information
