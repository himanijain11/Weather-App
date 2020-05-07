import requests
from django.shortcuts import render


def index(request):

    city = 'Agra'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={insert your API key}'

    if request.method=='POST':
        city = request.POST.get('city')

    r = requests.get(url.format(city)).json()
    city_weather= {
    'city':city,
    'temperature': r['main']['temp'],
    'description':r['weather'][0]['description'],
    'icon':r['weather'][0]['icon'],
    }
    context ={'city_weather':city_weather}
    return render(request,'index.html',context)
