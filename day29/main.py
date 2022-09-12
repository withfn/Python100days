from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

FONT_NAME = "Arial"
FONT_SIZE = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_account():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(email) == 0 or len(password == 0):
        messagebox.showerror(title="Fields Empty", message="You need fill all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                    f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", mode='a') as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20)

#logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


#label website
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_label.grid(row=1, column=0)

#label email/username
email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_label.grid(row=2, column=0)

#label password
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_label.grid(row=3, column=0)

#input website
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

#input email
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'thiago@gmail.com')

#input password
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky='w')

#button password
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=1, sticky='e')

#button add
add_button = Button(text="Add", width=36, command=add_account)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()