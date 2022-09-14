from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=300, highlightthickness=0)
        self.question = self.canvas.create_text(150, 150, text="", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=30, pady=40)
        
        self.score = Label(text=f"Score: ", font=('Arial', 18, 'italic'), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        
        self.cross_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_img, highlightthickness=0, command='')
        self.false_button.grid(row=2, column=0)
        
        self.right_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.right_img, highlightthickness=0, command='')
        self.true_button.grid(row=2, column=1)
        
        self.window.mainloop()
        
testezada = QuizInterface()