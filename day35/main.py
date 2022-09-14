import requests

LATITUDE = -23.525193
LONGITUDE = -46.823059

api_key ="c6a1785b783784e38f080a68032a34f2"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)