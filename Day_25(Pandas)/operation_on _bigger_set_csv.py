import pandas

data = pandas.read_csv("Day_25(Pandas)\Squirrel_Data.csv")

# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
new_data = data["Primary Fur Color"].value_counts()
print(new_data)
data_list = new_data.to_list()

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": data_list
}
data = pandas.DataFrame(data_dict)

data.to_csv("Day_25(Pandas)\color_data.csv")
