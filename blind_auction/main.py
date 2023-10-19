# importing system from os library for clear screen function
from os import system
import sys
print("Welcome to the blind auction --____--")

# creating a empty dictionary to add the bidders name and value
bidders = {}

def highest_bidder(bidders):
    # creating a variable to store highest bid
    highest_bid = 0
    # creating for loop to check highest bidder
    for i in bidders:
        bid_amount = bidders[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    system("cls")
    print(f"The winner is {winner} with the bid of ₹{bidders[winner]}")
    all_bids = input("You wanna a see all bids:").lower()
    if(all_bids == "yes"):
        print(bidders)
        print("Enter any Key to exit.")
        input()
    else:
        print("Enter any Key to exit.")
        input()

#creating a variable to for while loop exite
should_continue = True

# creating while loop so we can add as many bidders as we want
while(should_continue==True):

    # taking inputs of name and bid and adding it into bidders dictionary
    name = input("What is your name:\n")
    bid = int(input("Write your bid:\n₹ "))
    bidders[name] = bid
    more = input("Is there any more bidder type yes or no:\n").lower()
    if(more=="no"):
        should_continue = False
    else:
        system("cls") # clear screen function

highest_bidder(bidders)