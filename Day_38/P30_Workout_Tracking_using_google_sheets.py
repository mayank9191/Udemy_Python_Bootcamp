from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()
NLP_API_KEY = os.getenv("NLP_API_KEY")

natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/d3539dc12f0e96bd66153b168f8b4835/copyOfMyWorkouts/workouts"

headers = {
    "x-app-id": "7c09b3f5",
    "x-app-key": API_KEY
}

while (True):
    input_json = {
        "query": input("Tell me which exercises you did:"),
        "weight_kg": 70,
        "height_cm": 178,
        "age": 20
    }

    response = requests.post(url=natural_language_endpoint,
                             json=input_json, headers=headers)

    data = response.json()["exercises"][0]

    Duration = data["duration_min"]
    Calories = data["nf_calories"]
    Activity = data["name"]

    today_date = datetime.now().date().strftime("%d/%m/%Y")
    today_time = datetime.now().time().strftime("%H:%M:%S")

    input_json = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": Activity,
            "duration": Duration,
            "calories": Calories,
        }
    }
    response = requests.post(url=sheety_endpoint, json=input_json)

    print(response.text)
    print("Data Saved!")
