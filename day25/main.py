import turtle
from bank_states import BankStates

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=490)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

bank_states = BankStates()

game_is_on = True
while game_is_on:
    bank_states.answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    
    if bank_states.answer_state == 'off':
        game_is_on = False

screen.mainloop()