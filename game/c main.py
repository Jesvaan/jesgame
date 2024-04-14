import random
import tkinter as tk
from subprocess import call

# Create a new window
window = tk.Tk()

# Set the dimensions of the created window
window.geometry("600x400")

# Set the background color of the window
window.config(bg="#065569")

window.resizable(width=False, height=False)

# Set Window Title
window.title('Game World')


def OpenNG():
    call(["python", "c pro.py"])

def OpenTC():
    call(["python", "wordguess.py"])

def OpenWG():
    call(["python", "python qa.py"])


title = tk.Label(window, text="Jesvaan's Playground", font=("Arial", 24), fg="#fffcbd", bg="#065569")
title.place(x=140, y=50)

number_guess = tk.Button(window, text="It's Just Tic Tac Toe", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                        command=OpenNG)

tic_tac_toe = tk.Button(window, text="Guess it with Letters", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                        command=OpenTC)
word_guessing = tk.Button(window, text="Guess the number", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                        command=OpenWG)


number_guess.place(x=190, y=120)
tic_tac_toe.place(x=190, y=220)
word_guessing.place(x=200, y=320)

window.mainloop()
