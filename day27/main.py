import tkinter

def button_clicked():
    label_result["text"] = str(1.60934 * float(input.get()))

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=30)

label_miles = tkinter.Label(text="Miles", font=("Arial", 14))
label_miles.grid(row=0, column=2)
label_miles.config(padx=5, pady=5)

label_equal = tkinter.Label(text="is equal to", font=("Arial", 14))
label_equal.grid(row=1, column=0)
label_equal.config(padx=5, pady=5)

label_result = tkinter.Label(text="0", font=("Arial", 14))
label_result.grid(row=1, column=1)
label_result.config(padx=5, pady=5)

label_km = tkinter.Label(text="Km", font=("Arial", 14))
label_km.grid(row=1, column=2)
label_km.config(padx=5, pady=5)

input = tkinter.Entry(width=15)
input.grid(row=0, column=1)

button_calculate = tkinter.Button(text="Calculate", width=15, command=button_clicked)
button_calculate.grid(row=2, column=1)
button_calculate.config(padx=5, pady=5)

window.mainloop()