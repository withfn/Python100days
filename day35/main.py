import requests
from twilio.rest import Client

account_sid = "account"
auth_token = "token"

LATITUDE = '-23.525193'
LONGITUDE = '-46.823059'
lat_lon = ','.join([LATITUDE, LONGITUDE])
api_key ="api"

parameters = {
    "key": api_key,
    "q": lat_lon,
}

response = requests.get(url="http://api.weatherapi.com/v1/forecast.json", params=parameters)
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["forecast"]["forecastday"][0]["hour"][0:13]

will_rain = False

for hour_data in weather_slice:
    if hour_data["chance_of_rain"] >= 70:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. remember to bring an umbrella☔",
        from_='',
        to=''
    )
    print(message.status)