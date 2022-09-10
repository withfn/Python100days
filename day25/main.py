import turtle
from writer import Writer

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=490)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Writer()
guessed_states = len(writer.guessed_states)

while guessed_states < 50:
    writer.answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    
    if writer.answer_state == "Exit":
        break
    
    if writer.get_position():
        writer.update_states()

writer.states_to_learn()