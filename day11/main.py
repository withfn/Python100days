from essential import clear, logo
from random import choice, sample

def sum_cards(player):
    cards_temp = 0
    for card in player[0]:
        if card == 'A': cards_temp += 11   
        elif card == 'J' or card == 'Q' or card == 'K': cards_temp += 10
        else: cards_temp += card
    if 'A' in player[0]:
        for card in player[0]:
            if card == 'A' and cards_temp > 21: cards_temp -= 10
                    
    score = player[1]['sum'] = cards_temp
    return score

def compare(player_score, computer_score):
        if player_score == computer_score: return "Draw"
        
        elif computer_score == 21: return "Lose, Your opponent has Blackjack!"
        
        elif player_score == 21: return "You win with a Blackjack!"
        
        elif player_score > 21: return "You went over. You lose."
            
        elif computer_score > 21: return "Opponent went over. You win!"
        
        elif player_score > computer_score: return "You win!"
    
        else: return "You lose."

def play_game():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    print(logo)
    player_cards = [sample(cards, 2), {"sum":0}]
    computer_cards = [sample(cards, 2), {"sum":0}]
    
    should_continue = True
    while should_continue:
        player_score = sum_cards(player_cards)
        computer_score = sum_cards(computer_cards)
        print(f"Your cards: {player_cards[0]}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0][0]}")
        
        if player_score >= 21 or computer_score == 21: break
        
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y': player_cards[0].append(choice(cards))
        else: should_continue = False
    
    print(f"Your final hand: {player_cards[0]}, final score: {player_score}")

    while True:
        computer_score = sum_cards(computer_cards)
        if player_score < 21 and computer_score < 17:
                computer_cards[0].append(choice(cards))
        else: break
            
            
    print(f"computer's final hand {computer_cards[0]}, final score: {computer_score}")
    
    print(compare(player_score, computer_score))


clear()
print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
    