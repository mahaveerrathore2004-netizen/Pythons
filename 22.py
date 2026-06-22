a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

"""from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Main window
root = Tk()
root.title("Calculator")
root.geometry("300x400")

# Display
entry = Entry(root, width=20, font=("Arial", 20), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        Button(root, text=button, width=6, height=2, command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=button, width=6, height=2, command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
Button(root, text="C", width=26, height=2, command=clear).grid(row=row, column=0, columnspan=4)

root.mainloop()"""