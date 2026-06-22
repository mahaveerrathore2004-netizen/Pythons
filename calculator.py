from tkinter import *

# Button click function
def press(num):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(num))

# Equal button function
def equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")

# Clear function
def clear():
    display.delete(0, END)

# Main window
root = Tk()
root.title("Real Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Display screen
display = Entry(root, font=("Arial", 24), bd=10, relief=RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=8, height=3, command=equal).grid(row=row, column=col)
    else:
        Button(root, text=text, width=8, height=3,
               command=lambda t=text: press(t)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=35, height=3, command=clear).grid(row=5, column=0, columnspan=4)

# Run app
root.mainloop()