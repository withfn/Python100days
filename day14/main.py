from essential import clear
from game_data import data
from art import logo, vs
from random import shuffle

#Call the celebrity list and shuffle.
data_list = data
shuffle(data_list)

#returns celebrity as a formatted string.
def format_print(celebrity):
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}"

#finds the celebrity with the most followers and compares it to the user's answer, returning 'True' if the answer is correct.
def compare_answer(a, b, user):
    if data_list[a]['follower_count'] > data_list[b]['follower_count']:
        answer = 'a'
    else: 
        answer = 'b'
    
    if user != answer:
        return False
    return True

#start the game.
def game():
    a = 0
    b = 1
    run = True
    score = 0
    print(logo)
    
    while run:
        #shows the celebrities to be compared.
        print(f"Compare A: {format_print(data_list[a])}")
        print(vs)
        print(f"Against B: {format_print(data_list[b])}")

        #shows the celebrities to be compared.
        user = input("Who has more followers? Type 'A' or 'B': ").lower()
        run = compare_answer(a, b, user)
        
        if run:
            a += 1
            b += 1
            score += 1
            
            clear()
            print(logo)
            print(f"You're right! Current Score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong, Final Score: {score}.")
            
        if b == len(data_list):
            print(f"Congratulations, you've reached the end.\nFinal Score: {score}.")
            run = False
        
game()