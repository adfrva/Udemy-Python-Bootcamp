import random

print("Welcome to Rock, Paper, Scissors")

exitLoop = 0

while exitLoop == 0:
    choices = ["Rock", "Paper", "Scissors"]
    print("Type 'Exit' to exit game.\n")
    userChoice = input("Pick your hand: Rock, Paper, or Scissors\n")
    computerPickInt = random.randint(0,2)

    computerChoice = choices[computerPickInt]

    if userChoice == "Exit":
        exitLoop = 1

    if userChoice == computerChoice:
        print("Its a tie!")
    elif userChoice == "Rock" and computerChoice == "Paper":
        print("You win!")
    elif userChoice == "Paper" and computerChoice == "Rock":
        print("You Win!")
    elif userChoice == "Scissors" and computerChoice == "Paper":
        print("You Win!")
    else:
        print("You Lose :(")