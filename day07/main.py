from random import choice
from essential import clear, stages, logo,  word_list

chosen_word = choice(word_list)
guess = []
lives = 6
for x in chosen_word:
    guess += "_"

print(logo)

while True:
    player_guess = input("Guess a letter: ").lower()
    clear()
    if player_guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == player_guess:
                guess[letter] = chosen_word[letter]
    else:
        print(f"{player_guess} is not in the word, you lost 1 life")
        lives -= 1
    
    print(stages[lives])
    print(' '.join(guess) +'\n')

    if lives == 0:
        print('You lose.')
        break
    if not '_' in guess:
        print('You Win!') 
        break
print("Word: " + chosen_word)
print('\n\n')