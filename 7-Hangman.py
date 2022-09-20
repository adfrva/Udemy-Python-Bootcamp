import random

print("Welcome to Hangman\n")

def listToString(list): 
    string = " "
    
    return (string.join(list))

def stringToList(string):
    return list(string)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["Safaera", "Normans", "Hamilton", "KillerKlowns", "BadBunny", "Liverpool"]
randomWordString = random.choice(words)
randomWordList = stringToList(randomWordString)

wordLength = len(randomWordString)

solvedWordList = []

for n in range(0, wordLength):
    solvedWordList.append("_ ")

hangmanLives = 6

lettersGuessed = 0
gameOver = 0

while not gameOver:

    if hangmanLives == 0:
        gameOver = 1
        print(stages[0])
        print("Game over :(\n")
        break

    solvedWordStr = listToString(solvedWordList)

    print(stages[hangmanLives])

    print(solvedWordStr + "\n")

    userInput = input("Guess a letter or type 'exit'\n")

    if  userInput == "exit":
        gameOver = 1
        break

    else:
        guessCorrect = 0

        for n in range(0, wordLength):
            if randomWordList[n].lower() == userInput.lower():
                solvedWordList[n] = randomWordList[n]
                guessCorrect = 1
                lettersGuessed += 1

        if guessCorrect == 0:
            print("Wrong!\n")
            hangmanLives -= 1

        else:

            if lettersGuessed == wordLength:
                print("You Win!\n")
                print(solvedWordStr + "\n")
                gameOver = 1
                break
            else:
                print("Correct!\n")