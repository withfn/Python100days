from data_manager import DataManager
from notification_manager import NotificationManager


dataManager = DataManager()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

#dataManager.verify_iata_code()

for destination in dataManager.places:
    flight = dataManager.get_search(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
