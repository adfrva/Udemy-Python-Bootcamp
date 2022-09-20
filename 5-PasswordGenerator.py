import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

print("Hello to the Random Password Generator!")

letterCount = input("How many letters would you like in your password?\n")
symbolCount = input("How many symbols would you like in your password?\n")
numCount = input("How many numbers would you like in your password?\n")

intLetterCount = int(letterCount)
intSymbolCount = int(symbolCount)
intNumCount = int(numCount)
finalPassword = ""

#totalLen = intLetterCount + intSymbolCount + intNumCount

for i in range(0, intLetterCount):
    finalPassword = finalPassword + random.choice(letters)

for i in range(0, intSymbolCount):
    finalPassword = finalPassword + random.choice(symbols)

for i in range(0, intNumCount):
    finalPassword = finalPassword + random.choice(numbers)

finalPassword = shuffle_word(finalPassword)

print("Here is your password: " + finalPassword)