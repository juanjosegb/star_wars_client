from django.contrib.sites import requests


def get_vehicle(url):
    r = requests.get(url)
    vehicle = r.json()
    vehicle_information = dict()
    vehicle_information['name'] = vehicle['name']
    vehicle_information['model'] = vehicle['model']
    vehicle_information['manufacturer'] = vehicle['manufacturer']
    vehicle_information['cost_in_credits'] = vehicle['cost_in_credits']
    vehicle_information['length'] = vehicle['length']
    vehicle_information['max_atmosphering_speed'] = vehicle['max_atmosphering_speed']
    vehicle_information['crew'] = vehicle['crew']
    vehicle_information['passengers'] = vehicle['passengers']
    vehicle_information['cargo_capacity'] = vehicle['cargo_capacity']
    vehicle_information['consumables'] = vehicle['consumables']
    vehicle_information['vehicle_class'] = vehicle['vehicle_class']
    vehicle_information['pilots'] = vehicle['pilots']
    vehicle_information['films'] = vehicle['films']
    return vehicle_information
