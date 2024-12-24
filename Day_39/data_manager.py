import requests

sheety_endpoint = "https://api.sheety.co/7858ded2411a1df1a7e13982c132b1a7/copyOfFlightDeals/prices"


class Data_manager:
    # TO GET ROWS FROM A SHEET

    def get_from_sheet(self):
        '''It return json '''
        response = requests.get(url=sheety_endpoint)
        sheet_data = response.json()["prices"]
        return sheet_data

    # TO ADD A ROW IN A SHEET(POST)

    def sheet_input(self, **kwargs):
        '''It takes city name, iata code and lowest price and returns nothing'''
        input_json = {
            "price": kwargs,

        }
        response = requests.post(url=sheety_endpoint, json=input_json)

        print(response.text)

    # TO EDIT A ROW IN A SHEET (PUT)

    def edit_row(self, row: int, **kwargs):
        '''Edits a row by its id returns nothing'''

        input_json = {
            "price": kwargs
        }

        response = requests.put(
            url=f"{sheety_endpoint}/{row}", json=input_json)

        print(response.text)

    # TO DELETE A ROW IN GOOGLE SHEET WITH SHEETY WITH OBJECTID

    def delete_row(self, row: int):
        '''It deletes a row by its id returns nothing'''
        response = requests.delete(url=f"{sheety_endpoint}/{row}")
        print(response.text)
