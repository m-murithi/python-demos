import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0e21b3e0af27e0f4d0564b7897617ca3"


weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

