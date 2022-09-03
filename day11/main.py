from essential import clear, logo
from random import choice, sample

def sum_cards(player):
    cards_temp = 0
    for card in player[0]:
        if card == 'A':
            if cards_temp <= 10:
                cards_temp += 11
            else:
                cards_temp += 1     
        elif card == 'J' or card == 'Q' or card == 'K':
            cards_temp += 10
        else:
            cards_temp += card
    player[1]['sum'] = cards_temp
    
def print_cards(player_cards, computer_cards):
    print(f"Your cards: {player_cards[0]}, current score: {player_cards[1]['sum']}")
    print(f"Computer's first card: {computer_cards[0][0]}")
    
def blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    print(logo)
    player_cards = [sample(cards, 2), {"sum":0}]
    computer_cards = [sample(cards, 2), {"sum":0}]
    
    should_continue = True
    while should_continue:
        sum_cards(player_cards)
        print_cards(player_cards, computer_cards)
        
        if player_cards[1]['sum'] >= 21 or computer_cards[1]['sum'] == 21:
            break
        
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_cards[0].append(choice(cards))
        else:
            should_continue = False
    
    print(f"Your final hand: {player_cards[0]}, final score: {player_cards[1]['sum']}")
    if player_cards[1]['sum'] <= 21:
        while computer_cards[1]['sum'] < player_cards[1]['sum']:
            computer_cards[0].append(choice(cards))
    
    sum_cards(computer_cards)
    print(f"computer's final hand {computer_cards[0]}, final score: {computer_cards[1]['sum']}")
    
    if player_cards[1]['sum'] == computer_cards[1]['sum']:
        print("Draw!")
    
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()