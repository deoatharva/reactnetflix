import tkinter as tk
import random
from tkinter import messagebox

class MinesweeperGame:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0] * cols for _ in range(rows)]
        self.buttons = [[None] * cols for _ in range(rows)]
        self.game_over = False

        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.frame, width=2, command=lambda r=r, c=c: self.click(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

    def place_mines(self):
        mines = 0
        while mines < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = -1  # -1 represents a mine
                mines += 1

    def calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and self.board[r + dr][c + dc] == -1:
                            count += 1
                self.board[r][c] = count

    def click(self, r, c):
        if self.game_over:
            return

        if self.board[r][c] == -1:
            self.game_over = True
            self.buttons[r][c].config(text='*', relief=tk.SUNKEN, state=tk.DISABLED)
            self.show_all_mines()
            messagebox.showinfo("Game Over", "You lost!")
        else:
            self.reveal(r, c)

    def reveal(self, r, c):
        if self.board[r][c] != 0:
            self.buttons[r][c].config(text=str(self.board[r][c]), relief=tk.SUNKEN, state=tk.DISABLED)
        else:
            self.buttons[r][c].config(relief=tk.SUNKEN, state=tk.DISABLED)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and self.buttons[r + dr][c + dc]['state'] == tk.NORMAL:
                        self.reveal(r + dr, c + dc)

    def show_all_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    self.buttons[r][c].config(text='*', relief=tk.SUNKEN)

    def restart_game(self):
        self.game_over = False
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.place_mines()
        self.calculate_numbers()

        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].config(text='', relief=tk.RAISED, state=tk.NORMAL)

def main():
    rows = 8
    cols = 8
    num_mines = 10

    root = tk.Tk()
    root.title("Minesweeper")
    game = MinesweeperGame(root, rows, cols, num_mines)
    root.mainloop()

if __name__ == "__main__":
    main()

