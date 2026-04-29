"""
A simple guessing game with a small UI using tkinter.
Pick a number from 1 to 100 and try to guess it!
"""

import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("300x200")
        self.resizable(False, False)
        self.number = random.randint(1, 100)
        self.attempts_left = 5

        self.label = tk.Label(self, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.status = tk.Label(self, text=f"Attempts left: {self.attempts_left}")
        self.status.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")
            return

        if guess < 1 or guess > 100:
            messagebox.showwarning("Out of range", "Please guess a number between 1 and 100.")
            return

        self.attempts_left -= 1

        if guess == self.number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            self.reset_game()
        elif self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The number was {self.number}.")
            self.reset_game()
        elif guess < self.number:
            self.status.config(text=f"Too low! Attempts left: {self.attempts_left}")
        else:
            self.status.config(text=f"Too high! Attempts left: {self.attempts_left}")

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts_left = 5
        self.status.config(text=f"Attempts left: {self.attempts_left}")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()