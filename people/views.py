from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
import requests

def send_req(url):
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    return False


def upd_data(data):
    films = data['films']
    vehicles = data['vehicles']
    starships = data['starships']
    new_films = []
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])
        
    new_vehicles = []
    for vehicle in vehicles:
        vehicle = send_req(vehicle)
        new_vehicles.append(vehicle['name'])
        
    new_starships = []
    for starship in starships:
        starship = send_req(starship)
        new_starships.append(starship['name'])

    data['films'] = new_films
    data['vehicles'] = new_vehicles
    data['starships'] = new_starships

    return data


def get_luke_info(request):
    data = send_req('https://swapi.dev/api/people/1')
    if data:
        upda_data = upd_data(data)

        return render(request, 'people/person.html', upda_data)
    else:
        return HttpResponse('Ну чет не получилось')