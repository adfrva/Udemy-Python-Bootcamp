import os
import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack!")

def deal_cards():
    dealt_cards = []

    for i in range(2):
        random_card = random.choice(cards)
        dealt_cards.append(random_card)

    return dealt_cards

def add_card(array):
    random_card = random.choice(cards)

    array.append(random_card)

    return array

def check_hands(user_cards, computer_cards):
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    if user_sum == computer_sum:
        print("Its a Draw!")
    elif user_sum > 21 or computer_sum == 21:
        print("You Lose :(")
    elif user_sum == 21 or computer_sum > 21:
        print("You Win!")
    elif user_sum < computer_sum:
        print("You Lose :(")
    else:
        print("You Win!")

game_over = False

while not game_over:
    exit_prompt = input("Would you like to play blackjack? Yes or No? ")

    if exit_prompt.lower() == "no":
        game_over = True
    
    else:
        os.system("cls")

        user_cards = []
        computer_cards = []

        user_cards = deal_cards()
        computer_cards = deal_cards()

        print(f"Your final hand: {user_cards} = {sum(user_cards)}")
        print("Computer's first card: " + str(computer_cards[0]))

        deal_prompt = input("Type 'y' to deal another card. Type 'n' to pass ")

        if deal_prompt.lower() == 'n':
            print(f"Your final hand: {user_cards} = {sum(user_cards)}") 
            print(f"Computer's final hand: {computer_cards} = {sum(computer_cards)}")

            check_hands(user_cards, computer_cards)
        else:
            user_cards = add_card(user_cards)
            computer_cards = add_card(computer_cards)

            print(f"Your final hand: {user_cards} = {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards} = {sum(computer_cards)}")

            check_hands(user_cards, computer_cards)
