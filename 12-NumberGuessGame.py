import random

print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ")

lives = 0
random_num = random.randint(1, 100)
game_over = False

if difficulty.lower() == "easy":
    lives = 10

elif difficulty.lower() == "hard":
    lives = 5

else:
    print("Try again")

while not game_over:

    if lives == 0:
        game_over = False
        print("Game over :<")

    else:
        print(f"You have {lives} lives left")
        guess = input("Guess a number: ")

        if random_num == int(guess):
            print("Thats correct!")
            game_over = True

        elif random_num > int(guess):
            print("Thats too low!")
            lives -= 1
        
        else:
            print("Thats too high!")
            lives -= 1