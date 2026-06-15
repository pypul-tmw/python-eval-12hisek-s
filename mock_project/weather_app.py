import requests

def get_weather(city):
    url = f"https://api.weather.com/(city)"
    response = requests.get(url)
    return response.json()