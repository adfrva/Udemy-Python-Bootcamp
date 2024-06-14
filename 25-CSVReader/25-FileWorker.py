#with open('weather_data.csv') as data_file:
#    data = data_file.readlines()
#    print(data)
# Basic reading lines


# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# Basic temperature reading from file


import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
total_sum = sum(data["temp"])
print(f"Total sum of temps: {total_sum}")
total_temps = len(data["temp"])
print(f"Total number of temps recorded: {total_temps}")

average_temp = total_sum/total_temps

print(f"Average temperature: {average_temp}")