from essential_functions import clear, sleep, logo


print(logo)
print("Welcome to the secret auction program")
sleep(3)
clear()

bidders = {}
while True:
    name = input("What is your name?: ").capitalize()
    bid = int(input("What's your bid?: "))
    bidders[name] = bid

    add_bid =  input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clear()
    if not add_bid == "yes":
        break
highest_bid =max(bidders, key=bidders.get)
print(f"The winner is {highest_bid} with a bid of ${bidders[highest_bid]}")