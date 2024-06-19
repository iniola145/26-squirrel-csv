# # with open("./002 weather-data.csv") as data_file:
# #     weather_data = data_file.readlines()
#
# # import csv
# #
# # with open("./002 weather-data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
#
# import pandas
# data = pandas.read_csv("002 weather-data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # sum_num = 0
# #
# #
# # print(data["temp"].mean())
# # max_num = data["temp"].max()
# # print(max_num)
# # print(data.temp)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# Tuesday = data[data.day == "Tuesday"]
# temperatur_tue = Tuesday.temp
# temp_tue_F = (temperatur_tue * 1.8) + 32
# print(temp_tue_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas


data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

Grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(Grey_squirrel_count)
Cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Cinnamon_squirrel_count)
Black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(Black_squirrel_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [Grey_squirrel_count, Cinnamon_squirrel_count, Black_squirrel_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
print(data_frame)
