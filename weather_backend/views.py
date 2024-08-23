import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_weather(request, city):
    api_key = 'fb9933d59dc1f65fce1535983b917e49'  # Replace with your OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    print(data)
    return Response(data)

@api_view(['GET'])
def get_coordinates_weather(request, lat, long):
    api_key = 'fb9933d59dc1f65fce1535983b917e49'  # Replace with your OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=metric'
    print(url)
    response = requests.get(url)
    data = response.json()
    print(data)
    return Response(data)

