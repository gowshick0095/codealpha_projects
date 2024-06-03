import random
import tkinter as tk
from tkinter import messagebox

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.config(bg="pale turquoise")
        self.master.title("Hangman Game")
        self.word = random.choice(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"])
        self.guesses = set()
        self.remaining_attempts = 10

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Welcome to Hangman Game!",font=('Arial', 50),fg="dark green",bg="pale turquoise")
        self.instruction_label.place(x=350,y=100)

        self.guess_label = tk.Label(self.master, text="Enter your Guess:",font=('Arial', 30),fg="gray2",bg="pale turquoise")
        self.guess_label.place(x=350,y=250)

        self.guess_entry = tk.Entry(self.master,font=('Arial', 30),fg="gray2",bg="pale turquoise")
        self.guess_entry.place(x=700,y=250)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess,font=('Arial', 30),fg="gray2",bg="pale turquoise")
        self.submit_button.place(x=650,y=350)

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        elif guess in self.word:
            self.guesses.add(guess)
            self.update_display()
        else:
            self.guesses.add(guess)
            self.remaining_attempts -= 1
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you're out of attempts! The word was '{self.word}'.")
                self.master.destroy()
            else:
                messagebox.showinfo("Incorrect Guess", f"Wrong guess! You have {self.remaining_attempts} attempts left.")

    def update_display(self):
        display_word = "".join([letter if letter in self.guesses else "_" for letter in self.word])
        if display_word == self.word:
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}")
            self.master.destroy()
        else:
            messagebox.showinfo("Correct Guess", f"Correct guess! Current word: {display_word}")

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = Hangman(root)
    root.mainloop()
