print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? "))
percentageTip = float(input("\nWhat percentage tip would you like to give? 10, 12, or 15? "))
peopleToSplit = float(input("\nHow many people to split the bill? "))

billForEach = round((bill + (bill * percentageTip / 100)) / peopleToSplit, 2)

print(f"Each person should pay: ${billForEach}")