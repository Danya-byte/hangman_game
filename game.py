import tkinter as tk
from tkinter import messagebox
from faker import Faker
import random


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.fake = Faker()
        self.word = self.generate_random_word()  # Случайное слово
        self.guessed_letters = []
        self.attempts_left = 6

        self.create_widgets()

    def generate_random_word(self):
        # Генерируем случайное слово
        return self.fake.word().upper()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text=self.get_masked_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=20)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}", font=("Helvetica", 18))
        self.attempts_label.pack(pady=20)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=20)

    def get_masked_word(self):
        masked_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        return masked_word

    def make_guess(self):
        guess = self.entry.get().upper()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Duplicate Guess", "You already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

        self.word_label.config(text=self.get_masked_word())

        if self.attempts_left == 0:
            self.show_game_over_message()

        if "_" not in self.get_masked_word():
            self.show_good_job_message()

    def show_game_over_message(self):
        messagebox.showinfo("Game Over", f"You lost! The word was {self.word}.")
        self.disable_game()

    def show_good_job_message(self):
        messagebox.showinfo("Good Job", "You won!")
        self.disable_game()

    def disable_game(self):
        self.entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.word = self.generate_random_word()
        self.guessed_letters = []
        self.attempts_left = 6

        self.word_label.config(text=self.get_masked_word())
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()