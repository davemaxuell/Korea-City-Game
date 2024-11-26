# with open("weather_data - Sheet1.csv") as data_file:
#     data = data_file.readlines()
#
#     print(data)

# import csv
#
# with open("weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     tempretures = []
#     for row in data:
#         if row[1] != "temp":
#             tempretures.append(int(row[1]))
#
#     print(tempretures)

import pandas

data = pandas.read_csv("weather_data - Sheet1.csv")
# data_dictver = data.to_dict()
# print(data_dictver)
#
# data_listver = data["temp"].to_list()
# print(data_listver)
#
# print(data[data.day == "Monday"])
# print(data[data.temp  == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp * (9/5) + 32)