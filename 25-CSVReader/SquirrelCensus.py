import pandas

data = pandas.read_csv("2018_Squirrel_Census.csv")

gray_count = 0
red_count = 0
black_count = 0


#For loop through dataframe rows
for index, row in data.iterrows():
    color = row['Primary Fur Color']
    if color == 'Gray':
        gray_count += 1
    elif color == 'Cinnamon':
        red_count += 1
    elif color == 'Black':
        black_count += 1

count_data = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Total": [gray_count, red_count, black_count]

}

total_frame = pandas.DataFrame(count_data)

total_frame.to_csv("Color_Totals.csv")

print(f"Gray count: {gray_count}")
print(f"Red Count: {red_count}")
print(f"Black Count: {black_count}")



#
#Better way to complete
#
# data = pandas.read_csv("2018_Squirrel_Census.csv")
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
#
# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("Color_Totals2.csv")