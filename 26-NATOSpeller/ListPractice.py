#new_list = [new_item for item in list]
numbers = [1,2,3]

#Create new list that is values in numbers list +1

new_numbers = [num + 1 for num in numbers]

print(new_numbers)

#Given a range of nums, return a new list of nums in range*2
range_mult = [num * 2 for num in range(1, 5)]
print(range_mult)


#new_list = [new_item for item in list if whatever]

names = ["Jeff", "Mikey", "Flanders", "Fred"]
#Create list of only names with characters less than 5
short_names = [name for name in names if len(name) < 5]
print(short_names)

#Create new list containing all names from other list but all caps
cap_names = [name.upper() for name in names]
print(cap_names)