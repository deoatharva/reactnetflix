import tkinter as tk

class QueensGame:
    def __init__(self, master):
        self.master = master
        self.master.title("4 Queens Game")
        self.board_size = 4
        self.queens = []  # To store positions of queens

        # Initialize the chessboard GUI
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_board()

        # Bind click event to canvas
        self.canvas.bind("<Button-1>", self.place_queen)

    def draw_board(self):
        # Draw the chessboard
        for i in range(self.board_size):
            for j in range(self.board_size):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill=color)

    def place_queen(self, event):
        # Calculate the position clicked
        col = event.x // 100
        row = event.y // 100

        # Check if placing the queen is valid
        if self.is_valid_position(row, col):
            self.queens.append((row, col))
            self.draw_queen(row, col)

            # Check if game is won
            if len(self.queens) == self.board_size:
                print("Congratulations! You placed all 4 queens.")
                self.canvas.unbind("<Button-1>")  # Disable further clicks

    def is_valid_position(self, row, col):
        # Check if placing a queen at (row, col) is valid
        for (r, c) in self.queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def draw_queen(self, row, col):
        # Draw a queen on the board at (row, col)
        x0, y0 = col * 100 + 10, row * 100 + 10
        x1, y1 = x0 + 80, y0 + 80
        self.canvas.create_oval(x0, y0, x1, y1, fill="blue")
    
    def reset_game(self):
        self.queens = []
        self.canvas.delete("all")
        self.draw_board()
        self.canvas.bind("<Button-1>", self.place_queen)


if __name__ == "__main__":
    root = tk.Tk()
    game = QueensGame(root)
    
    # Add a button to reset the game
    reset_button = tk.Button(root, text="Reset Game", command=game.reset_game)
    reset_button.pack()
    
    root.mainloop()
