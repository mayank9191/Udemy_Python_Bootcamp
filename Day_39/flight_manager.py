from dotenv import load_dotenv
import os
import requests

load_dotenv()
url = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"


class Flight_manager:
    def airport_details(self, city: str):
        '''It returns the airport IATA code and airport name'''
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"
        querystring = {"query": city,
                       "locale": "en-US"}

        headers = {
            "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
            "x-rapidapi-host": os.getenv("RAPID_API_HOST")
        }

        try:
            response = requests.get(
                url=url, headers=headers, params=querystring)

            airport = response.json()["data"][0]["presentation"]["title"]
            iataCode = response.json()["data"][0]["skyId"]

            return {"iataCode": iataCode, "airport": airport}

        except KeyError:
            print("Error")

    def cheap_flight(self, destination: str, origin: str = "DEL"):
        '''It returns cheap flight and date of departure'''
        querystring = {"fromEntityId": origin,
                       "toEntityId": destination,
                       "departDate": "2025-02-11",
                       "currency": "INR"}

        headers = {
            "x-rapidapi-key": "c8685ed932msh261d6c99255a673p15bde6jsna0b10c91124e",
            "x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return [response.json()["data"][0], response.json()["data"][1], response.json()["data"][2]]


# flight = Flight_manager()

# print(flight.airport_details("istanbul"))
# print(flight.cheap_flight("ISTA"))
