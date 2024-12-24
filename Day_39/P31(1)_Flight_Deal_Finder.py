import data_manager
import flight_manager
import notification_manager

data = data_manager.Data_manager()
flight = flight_manager.Flight_manager()
notify = notification_manager.Notification()


def delete_row(id: int = 2):
    data.delete_row(id)


def cheap_price_auto_inserter_into_sheet():

    for i in range(len(data.get_from_sheet())):
        try:
            dest_iata = data.get_from_sheet()[i]["iataCode"]
            cheap_price_info = flight.cheap_flight(destination=dest_iata)[0]
            price = cheap_price_info["price"]
            data.edit_row(lowestPrice=price, row=i+2)

        except TypeError:
            data.edit_row(lowestPrice="n/a", row=i+2)


def iataCode_auto_inserter_into_sheet():
    for i in range(len(data.get_from_sheet())):
        iataCode = flight.airport_details(
            city=data.get_from_sheet()[i]["city"])
        data.edit_row(iataCode=iataCode["iataCode"], row=i+2)


def iataCode_insert(place):
    iataCode = flight.airport_details(city=place)
    return iataCode["iataCode"]


def cheap_price_insert(place):
    try:
        place_iataCode = iataCode_insert(place)
        cheap_price_info = flight.cheap_flight(destination=place_iataCode)
        return cheap_price_info[0]
    except TypeError:
        return "n/a"


def place_want_to_vist(place):
    data.sheet_input(city=place.upper(), iataCode=iataCode_insert(
        place), lowestPrice=cheap_price_insert(place)["price"], departDate=cheap_price_insert(place)["day"])


# List = ["bombay", "chennai", "hyderabad", "kolkata"]
# for i in List:
#     place_want_to_vist(i)

# iataCode_auto_inserter_into_sheet()

# cheap_price_auto_inserter_into_sheet()

def inform_for_cheap_price():
    for i in range(len(data.get_from_sheet())):
        place = data.get_from_sheet()[i]
        cheap_price_date = cheap_price_insert(place["city"])
        print(place["lowestPrice"])
        print(cheap_price_date["price"])

        if (place["lowestPrice"] > cheap_price_date["price"]):
            notify.notification(msg=f'''Low price alert! Only ₹{cheap_price_date["price"]} to fly from DELHI to {
                                place["city"]} on {cheap_price_date["day"]}''', number="+919315907657")

            data.edit_row(row=i+2, lowestPrice=cheap_price_date["price"])


inform_for_cheap_price()
