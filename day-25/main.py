# # import csv
# #
# # with open("weather_data.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #  Get data in columns
# print(data["condition"])
# print(data.condition)
#
# #  get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_F = (monday.temp * 9/5) + 32
# print(monday_temp_F)
#
# #  Create dataframe form scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
processed_data = data[['Unique Squirrel ID', 'Primary Fur Color']].groupby(["Primary Fur Color"]).count()
processed_data["Unique Squirrel ID"].to_csv("squirrel_count.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, red_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv2")
