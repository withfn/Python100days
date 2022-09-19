from data_manager import DataManager

dataManager = DataManager()

ORIGIN_CITY_IATA = "LON"

#dataManager.verify_iata_code()

for destination in dataManager.places:
    flight = dataManager.get_search(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
    )
