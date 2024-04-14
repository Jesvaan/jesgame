import tkinter as tk
import random

class HangmanGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("800x600")  # Set the window size to 800x600
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
        self.word = random.choice(self.word_list)
        self.guesses = set()
        self.guesses_left = 10

        # Create a Label to display the word list
        self.word_list_label = tk.Label(self, text="Topic:fruit", font=("Helvetica", 24))
        self.word_list_label.pack()


        # Create the rest of the widgets for the game
        self.word_label = tk.Label(self, text="_" * len(self.word), font=("Helvetica", 32))
        self.word_label.pack(pady=50)

        self.guess_label = tk.Label(self, text=f"{self.guesses_left} guesses left", font=("Helvetica", 24))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self, font=("Helvetica", 24))
        self.guess_entry.pack(pady=20)

        self.submit_button = tk.Button(self, text="Guess", command=self.guess_letter, font=("Helvetica", 24))
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.result_label.pack()

    def guess_letter(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.guesses:
            return

        self.guesses.add(guess)

        if guess in self.word:
            new_word = ""
            for letter in self.word:
                if letter in self.guesses:
                    new_word += letter
                else:
                    new_word += "_"

            self.word_label.config(text=new_word, font=("Helvetica", 32))

            if "_" not in new_word:
                self.result_label.config(text="You won!", font=("Helvetica", 32))
                self.submit_button.config(state=tk.DISABLED)
                self.guess_entry.config(state=tk.DISABLED)
        else:
            self.guesses_left -= 1
            self.guess_label.config(text=f"{self.guesses_left} guesses left", font=("Helvetica", 24))

            if self.guesses_left == 0:
                self.result_label.config(text=f"You lost! The word was {self.word}.", font=("Helvetica", 32))
                self.submit_button.config(state=tk.DISABLED)
                self.guess_entry.config(state=tk.DISABLED)

root = tk.Tk()
game = HangmanGame(master=root)
game.mainloop()