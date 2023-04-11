from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
import datetime


# Create your views here.

def index(request):
    api_key = '10fbf22a02e8255aa2148a7853568814'
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            new_object = City(name=name)
            new_object.save()
    else:
        form = CityForm()
    city =City.objects.last()

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    city_weather = response.json()
    now = datetime.datetime.now()
    weather = {
        "city":str(city).title(), 
        "now":now,
        "main":city_weather["weather"][0]["main"],
        "temperature":round(int(city_weather["main"]["temp"])-273.15,1),
        "pressure":city_weather["main"]["pressure"],
        "humidity":city_weather["main"]["humidity"],
        "icon":city_weather["weather"][0]["icon"],
        "description":city_weather["weather"][0]["description"],
        "windspeed":city_weather["wind"]["speed"]
    }

    return render(request,"index.html",{
        "weather" : weather,
        "form": form,
    })