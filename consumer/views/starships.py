import requests



def get_starship(pk):
    url = 'http://swapi.co/api/starships/' + str(pk)
    r = requests.get(url)
    starship = r.json()
    starship_information = dict()
    starship_information['name'] = starship['name']
    starship_information['model'] = starship['model']
    starship_information['manufacturer'] = starship['manufacturer']
    starship_information['cost_in_credits'] = starship['cost_in_credits']
    starship_information['length'] = starship['length']
    starship_information['max_atmosphering_speed'] = starship['max_atmosphering_speed']
    starship_information['crew'] = starship['crew']
    starship_information['passengers'] = starship['passengers']
    starship_information['cargo_capacity'] = starship['cargo_capacity']
    starship_information['consumables'] = starship['consumables']
    starship_information['hyperdrive_rating'] = starship['hyperdrive_rating']
    starship_information['MGLT'] = starship['species']
    starship_information['starship_class'] = starship['starship_class']
    starship_information['pilots'] = starship['pilots']
    starship_information['films'] = starship['films']
    return starship_information
