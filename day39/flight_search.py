import requests
from datetime import datetime, timedelta

API_KEY = "066wYwVtzmgdPLv_pevt15Cw6LN1c0Ic"

date_from = datetime.now() + timedelta(days=1)
date_to = date_from + timedelta(days=180)

class FlightSearch:
    def __init__(self) -> None:
        self.flight_endpoint = "https://api.tequila.kiwi.com"
        self.headers = {"apikey": API_KEY}
        
        
    
    def get_search(self):
        search_endpoint = f"{self.flight_endpoint}/v2/search"
        parameters = {
            "fly_from": "LON",
            "fly_to": "PAR",
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "price_to": 66,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        request = requests.get(url=search_endpoint, params=parameters, headers=self.headers).json()["data"][0]
        print(request)
        
    def get_iataCode(self, place):
        config = { "term": place }
        location_endpoint = f"{self.flight_endpoint}/locations/query"
        request = requests.get(url=location_endpoint, params=config, headers=self.headers).json()
        return request["locations"][0]["code"]


teste = FlightSearch()
teste.get_search()