import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generatedPassword = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for x in range(nr_letters):
    generatedPassword.append(random.choice(letters))
    
for x in range(nr_symbols):
    generatedPassword.append(random.choice(symbols))

for x in range(nr_numbers):
    generatedPassword.append(random.choice(numbers))

random.shuffle(generatedPassword)

print(f"Here is your password: {''.join(generatedPassword)}")

if len(generatedPassword) <= 6:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
elif len(generatedPassword) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")
else:
    print("Your password is strong.")