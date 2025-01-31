import requests
from audio import speak

def get_weather(city_name):
    api_key = "" # Your weatherstack api key here.
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city_name
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "current" in data:
            speak(f"In {city_name} , Temperature is {data['current']['temperature']}°C , Weather is {', '.join(data['current']['weather_descriptions'])} , Humidity is {data['current']['humidity']}% , Wind speed is {data['current']['wind_speed']} km/h sir.")
        else:
            print(f"Unable to fetch weather data,Please try again later sir.")
    except Exception as e:
        speak(f"This feature is in developement sir.")
        
