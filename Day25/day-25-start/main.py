#with open("weather_data.csv") as data_file:
#   data = data_file.readline()
# print(data)

#import csv
#with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for row in data:
#      if print(row[1] != "temp"):
#         temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())

#get data in columns
print(data["condition"])
print(data.condition)

# get data in rows
print(data[data.day == "Monday"])
print(data[data.day == "Sunday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

# Create a dataframe a scratch

data_dict = {
    "students": ["Amy", "Angela", "Rayan"],
    "scores": [76, 67, 89]
}

data1 = pandas.DataFrame(data_dict)
data1.to_csv("new_data.csv")
