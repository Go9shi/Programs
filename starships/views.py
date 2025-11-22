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
    pilots = data['pilots']

    new_films = []
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])
    
    new_pilots = []
    for pilot in pilots:
        pilot = send_req(pilot)
        new_pilots.append(pilot['name'])


    data['films'] = new_films
    data['pilots'] = new_pilots

    return data


def get_x_wing_info(request):
    data = send_req('https://swapi.dev/api/starships/12')
    if data:
        upda_data = upd_data(data)

        return render(request, 'starships/starship.html', upda_data)
    else:
        return HttpResponse('Ну чет не получилось')


def get_imperial_shuttle_info(request):
    data = send_req('https://swapi.dev/api/starships/22')
    if data:
        upda_data = upd_data(data)

        return render(request, 'starships/starship.html', upda_data)
    else:
        return HttpResponse('Ну чет не получилось')


def get_droid_control_ship_info(request):
    data = send_req('https://swapi.dev/api/starships/32')
    if data:
        upda_data = upd_data(data)

        return render(request, 'starships/starship.html', upda_data)
    else:
        return HttpResponse('Ну чет не получилось')