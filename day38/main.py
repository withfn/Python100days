import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

SHEETY_BEARER_AUTH = ""

user_input = input("Tell me which exercises you did: ")
date = datetime.now()

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/e9f414f1608d1f169dabfa0579660f72/myWorkouts/workouts"

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
    }

sheety_headers = {"Authorization": SHEETY_BEARER_AUTH }
config_nutritionix = {
    "query": user_input
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=config_nutritionix, headers=nutri_headers)
workouts = nutritionix_response.json()["exercises"]

for workout in workouts:
    config_sheety = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%H:%M:%S"),
            "exercise": workout["name"].title(),
            "duration": round(workout["duration_min"]),
            "calories": round(workout["nf_calories"]),
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=config_sheety, headers=sheety_headers)