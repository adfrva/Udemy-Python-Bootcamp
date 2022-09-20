print("Welcome to the Tip Calculator")
totalCost = input("What was the total bill?\n")
splitNum = input("How many people are splitting the bill?\n")
tipPercent = input("What percentage tip would you like to give them? 10, 12, or 15?\n")

individualCost = float(totalCost)/float(splitNum)

tipAmount = individualCost * (float(tipPercent)/100)
tipTotal = individualCost + tipAmount

print("Each person should pay: $" + str(round(tipTotal, 2)))