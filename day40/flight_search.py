import requests
from datetime import datetime, timedelta
from flight_data import FlightData

API_KEY = "066wYwVtzmgdPLv_pevt15Cw6LN1c0Ic"

date_from = datetime.now() + timedelta(days=1)
date_to = date_from + timedelta(days=180)

class FlightSearch:
    def __init__(self) -> None:
        self.flight_endpoint = "https://api.tequila.kiwi.com"
        self.headers = {"apikey": API_KEY}
        
        
    
    def get_search(self, origin_city_code, destination_city_code):
        search_endpoint = f"{self.flight_endpoint}/v2/search"
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        
        flight_data =FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
        
    def get_iataCode(self, place):
        config = { "term": place }
        location_endpoint = f"{self.flight_endpoint}/locations/query"
        request = requests.get(url=location_endpoint, params=config, headers=self.headers).json()
        return request["locations"][0]["code"]


teste = FlightSearch()
teste.get_search()