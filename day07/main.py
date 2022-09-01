from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = choice(word_list)
guess = []
lives = 6
for x in chosen_word:
    guess += "_"

print(logo)

while True:
    print(stages[lives])
    player_guess = input("Guess a letter: ").lower()
    if player_guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == player_guess:
                guess[letter] = chosen_word[letter]
    else:
        lives -= 1
    print(' '.join(guess))

    if lives == 0:
        print('You lose.')
        break
    if not '_' in guess:
        print('You Win!') 
        break
print("Word: " + chosen_word)