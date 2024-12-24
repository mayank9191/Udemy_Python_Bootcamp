from dotenv import load_dotenv
import os
import requests
import datetime as dt

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

flight_search_endpoint = "https://test.api.amadeus.com/v2"


class Flight_manager:

    # TO GET AUTHORIZATION TOKEN
    def __init__(self):
        def get_authtoken():
            '''TO GET AUTHORIZATION TOKEN'''
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }

            body = {
                "grant_type": "client_credentials",
                "client_id": API_KEY,
                "client_secret": API_SECRET
            }
            response = requests.post(
                url=f"https://test.api.amadeus.com/v1/security/oauth2/token", data=body, headers=headers)

            access_token = response.json()["access_token"]
            return access_token
        token = get_authtoken()
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    # TO GET IATA CODE OF THE CITY

    def IataCode_finder(self, city: str, country_code: str = "IN"):
        '''City Name should be complete and country code should be according to country to travel default country INDIA return IATA code'''
        parameters = {
            "subType": "CITY",
            "keyword": city,
            "countryCode": country_code
        }
        try:
            response = requests.get(
                url=f"{flight_search_endpoint}/reference-data/locations", params=parameters, headers=self.headers)

            return response.json()["data"][0]["iataCode"]

        except KeyError:
            return "n/a"

    # TO GET CHEAP FLIGHT PRICE AND DEPARTURE DATES

    def cheap_flight_price(self, origin: str, destination: str):
        '''origin and destination should be there IATA code and returns dict'''
        parameter = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": "2024-12-17",
            "adults": 1,
            "currencyCode": "INR",
            "travelClass": "ECONOMY"

        }

        response = requests.get(
            url=f"{flight_search_endpoint}/shopping/flight-offers", params=parameter, headers=self.headers)

        flight_data = response.json()["data"]

        # lowest_price = flight_data[0]["price"]["total"]
        # departure_date = flight_data[0]["departureDate"]

        # return {"lowest_price": lowest_price, "departure_date": departure_date}
        for i in range(50):
            time = flight_data[i]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[
                1]
            duration = flight_data[i]["itineraries"][0]["duration"].split("T")[
                1]
            price = flight_data[i]["price"]["grandTotal"]
            print({"departure time": time, "Duration": duration, "grand Total": price})

        # except KeyError:
        #     # print(response.json()["errors"][0])
        #     return flight_data

    def flight_price(self, origin: str, destination: str, date: str, adult: int = 1, Class: str = "ECONOMY"):
        parameter = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": adult,
            "currencyCode": "INR",
            "travelClass": Class.upper()
        }

        response = requests.get(
            url=f"{flight_search_endpoint}/shopping/flight-offers", params=parameter, headers=self.headers)

        result = response.json()["meta"]["count"]
        print(f"total offers = {result}")
        flight_data = response.json()["data"]

        print(date)
        print(flight_data)
        # for i in range(10):
        #     flight_name = flight_data[i]["itineraries"][0]["segments"][0]

        #     flight_details = f'''{flight_name['carrierCode']}{
        #         flight_name['number']}'''

        #     print(flight_details)
        #     time = flight_data[i]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[
        #         1]
        #     duration = flight_data[i]["itineraries"][0]["duration"].split("T")[
        #         1]
        #     price = flight_data[i]["price"]["grandTotal"]
        #     print({"departure time": time,
        #           "Duration": duration, "grand Total": price})


flight = Flight_manager()

flight.cheap_flight(origin="DEL", destination="IST")
