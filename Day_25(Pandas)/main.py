# with open("Day_25\weather_data.csv") as f:
#     content = f.read()
#     data = content.splitlines()
#     print(data)

# import csv

# with open("Day_25\weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperatures = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperatures.append(int(row[1]))

#     print(temperatures)

import turtle as t
import pandas

data = pandas.read_csv("Day_25(Pandas)/weather_data.csv")
# print(data)
# print(data["temp"])
# Whole table is considered as Dataframes data type
# print(type(data))
# while a portion or column of a table is series data type
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = data["temp"].mean()
# print(average)

# largest = data["temp"].max()
# print(largest)

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print({(monday.temp * 9/5) + 32})

# Create a Dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("Day_25/new_data.csv")
