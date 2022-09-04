from essential import clear, logo
from random import choice

#return the difficulty select by the user
def difficulty():
    user_pick = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
    return 10 if user_pick == 'easy' else 5

#compares the numbers and returns if the game continues or not
def compare_numbers(guess):
    if user_guess == number_choice: 
        print(f"You got it! The answer was {number_choice}")
        return False
    elif user_guess > number_choice:
        print("Too high.")
    else:
        print("Too low.")
    return True
        
print(logo)
print("Welcome to the Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\nTry to guess it!\n")

number_choice = choice(range(100))
chances = difficulty()
game_continue = True

while game_continue == True:
    print(f"You have {chances} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    game_continue = compare_numbers(user_guess)
    
    if game_continue:
        if (chances - 1) > 0:
            chances -= 1
            print("Guess again\n")
        else: 
            print("You've run out of guesses, you lose.")
            game_continue = False
