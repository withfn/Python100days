from essential import clear, logo

bidders = {}
while True:
    print(logo)
    name = input("What is your name?: ").capitalize()
    bid = float(input("How much would you like to bid?: "))
    bidders[name] = bid

    add_bid =  input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clear()
    if not add_bid == "yes":
        break
highest_bid = max(bidders, key=bidders.get)
print(logo)
print("The winner is {} with a bid of ${:.2f}".format(highest_bid, bidders[highest_bid]))