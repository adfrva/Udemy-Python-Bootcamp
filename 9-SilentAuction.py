import os

print("Welcome to the Silent Auction\n")

auction_dictionary = {}
is_over = False

def find_max_bid(dictionary):
    highest_bid = 0
    highest_bidder = ""

    for bidder in dictionary:
        bid = dictionary[bidder]
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    highest_bid_str = highest_bidder + " $" + str(highest_bid)

    return(highest_bid_str)

while not is_over:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")

    auction_dictionary[name] = int(bid)
    
    user_prompt = input("Are there any other bidders? Yes or No?\n")

    if user_prompt.lower() == "no":
        is_over = True
        print("The highest bidder is: " + find_max_bid(auction_dictionary))
    else:
        os.system('cls')