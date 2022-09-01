import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handFigure = [rock, paper, scissors]
numberHand = ['Rock', 'Paper', 'Scissors']
computer = random.choice(range(0, 3))

playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if not playerChoice.isdigit():
    print("You've entered an invalid value, try again and choose a number between 0-2.")

else:
    playerChoice = int(playerChoice)
    print(f'Your choice: {numberHand[playerChoice]}\n{handFigure[playerChoice]}')
    print(f'Computer\'s Choice: {numberHand[computer]}\n{handFigure[computer]}')

    if playerChoice == computer:
        print('Draw!')
        
    if playerChoice == 0:
        if computer == 1:
            print('You Lose.')
        else:
            print('You Win!')

    if playerChoice == 1:
        if computer == 0:
            print('You Win!')
        else:
            print('You Lose.')
            
    if playerChoice == 2:
        if computer == 0:
            print('You Lose.')
        else:
            print('You Win!')