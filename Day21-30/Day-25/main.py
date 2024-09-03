# with open("./weather_data.csv") as data_file:
#     content = data_file.readlines()
#     data = [item.strip() for item in content]

# print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)``
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1].isdigit(): #or if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(data['temp'])



# data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))

# # avg = 0 
# # for _ in temp_list:
# #     avg +=_
# # avg = avg/len(temp_list)

# # avg = sum(temp_list)/len(temp_list)

# avg = data["temp"].mean()

# max = data["temp"].max()

# print(f"Average Temperature : <{avg}>")
# print(f"MAX Temperature : <{max}>")

# #  Get Data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# # print(monday.temp)
# F = (monday.temp[0]*9/5) + 32 
# print(f"Temp in F for Monday: {F}")


# Create a dataframe from scratch

# data_dict = {
#     "students" : ["Anuj", "James" , "Amy"],
#     "scores":[76,56,32]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Challenge create a new csv with Fur color , count

import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]

red=    len(data[data["Primary Fur Color"] == "Cinnamon"])
grey =  len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

# for _ in color:
#     if _ == "Cinnamon":
#         red +=1
#     elif _ == "Gray":
#         grey +=1
#     elif _ == "Black":
#         black+=1

new_dict = {
    "Fur_color" : [ 'red','grey','black'],
    "count" :  [red,grey,black],
    
}

new_Data = pandas.DataFrame(new_dict)

new_Data.to_csv("squirrel_count.csv")
