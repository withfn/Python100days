from flight_search import FlightSearch
import requests

BEARER_AUTH = "Bearer e4d15516139f4a0e91f1520391f7a26f"

class DataManager(FlightSearch):
    def __init__(self) -> None:
        super().__init__()
        self.sheety_endpoint = "https://api.sheety.co/e9f414f1608d1f169dabfa0579660f72/flightDeals/prices"
        self.headers = {"Authorization": BEARER_AUTH}
        self.places = requests.get(url=self.sheety_endpoint, headers=self.headers).json()["prices"]

    
    def verify_iata_code(self):
        for place in self.places:
            if place["iataCode"] == "":
                city = place["city"]
                iatacode = self.flightSearch.get_iataCode(city)
                endpoint = f"{self.sheety_endpoint}/{place['id']}"
                config = {
                    "price":{ "iataCode": iatacode },
                }
                requests.put(url=endpoint, json=config, headers=self.headers)
