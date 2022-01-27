import tkinter as tk
import random

app = tk.Tk()
app.title("Password Generator")
app.geometry("300x100")
app.resizable(False, False)

password_var = tk.StringVar()

passwordGeneratedEntry = tk.Entry(app, textvariable=password_var)
passwordGeneratedEntry.place(x=90, y=15)


def makeStrongPassword(var):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)
    string1 = alpha[random.randint(0, len(alpha) - 1)] + alpha[random.randint(0, len(alpha) - 1)] + alpha[
        random.randint(0, len(alpha) - 1)] + alpha[random.randint(0, len(alpha) - 1)]
    string2 = alpha[random.randint(0, len(alpha) - 1)] + alpha[random.randint(0, len(alpha) - 1)] + alpha[
        random.randint(0, len(alpha) - 1)] + alpha[random.randint(0, len(alpha) - 1)]
    string2 = string2.lower()
    password = (str(num1) + string1 + str(num2) + string2)
    var.set(password)


genPasswordButton = tk.Button(app, text="Generate Password", command= lambda: makeStrongPassword(password_var))
genPasswordButton.place(x=90, y=40)

app.mainloop()
