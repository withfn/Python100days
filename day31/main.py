from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
current_card = {}

#open data
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/portuguese_words.csv")
finally:
    to_learn = df.to_dict(orient="records")

#pick a random card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text='Portuguese', fill='black')
    canvas.itemconfig(word, text=current_card['portuguese'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)

#flip card
def flip_card():
    global current_card
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['english'], fill='white')
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
# ------------------------ UI SETUP ---------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
#card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400, 150, text="title", fill="black", font=TITLE_FONT)
word = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

#unknown_button
wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

#known_button
right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()