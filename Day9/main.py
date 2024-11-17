import os
from art import logoa
print(logoa)
bids = {}
bidding_finished = False
winner = ""
highest_bid = 0
def find_highest_bid(bidding_record):
    winner = ""
    highest_bid = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"winner is {winner} with bid amount ${highest_bid}")
def clear_screen():
    print("\n" * 100)
while not bidding_finished:
    name = input("What is your name: ")
    price = int(input("What is your bid : $"))
    bids[name] = price
    should_continue = input("Are there any bidders Type 'yes' or 'no' ")
    if should_continue.lower() == 'yes':
        clear_screen()
    else:
        bidding_finished=True
        find_highest_bid(bids)