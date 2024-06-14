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

    if userChoice.lower() == computerChoice.lower():
        print("Its a tie!")

    elif userChoice.lower() == "rock" and computerChoice == "Paper":
        print("You win! The computer chose " + computerChoice)

    elif userChoice.lower() == "paper" and computerChoice == "Rock":
        print("You Win! The computer chose " + computerChoice)

    elif userChoice.lower() == "scissors" and computerChoice == "Paper":
        print("You Win! The computer chose " + computerChoice)

    else:
        print("You Lose :( The computer chose " + computerChoice)
