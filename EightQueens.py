import tkinter as tk
from tkinter import messagebox

class EightQueensGame:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Queens Game")
        self.board_size = 8
        self.cell_size = 50
        self.board = [[0] * self.board_size for _ in range(self.board_size)]

        self.canvas = tk.Canvas(master, width=self.cell_size * self.board_size, height=self.cell_size * self.board_size)
        self.canvas.pack()

        self.queen_size = 40
        self.drag_data = {"x": 0, "y": 0, "item": None}

        self.setup_board()
        self.create_drag_drop()

    def setup_board(self):
        """Draw the chessboard and initial queens."""
        self.canvas.delete("all")
        for row in range(self.board_size):
            for col in range(self.board_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = 'white' if (row + col) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

        # Draw the initial queens
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == 1:
                    self.draw_queen(row, col)

    def draw_queen(self, row, col):
        """Draw a queen on the board."""
        x1 = col * self.cell_size + 5
        y1 = row * self.cell_size + 5
        x2 = x1 + self.queen_size
        y2 = y1 + self.queen_size
        queen = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline='black', tags="queen")
        self.canvas.tag_bind(queen, "<Button-1>", self.on_queen_click)
        self.canvas.tag_bind(queen, "<B1-Motion>", self.on_queen_drag)
        self.canvas.tag_bind(queen, "<ButtonRelease-1>", self.on_queen_drop)

    def create_drag_drop(self):
        """Create drag-and-drop functionality."""
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        """Handle the canvas click event to place or move queens."""
        row, col = self.get_grid_coords(event.x, event.y)
        if self.is_valid_placement(row, col):
            self.board[row][col] = 1
            self.setup_board()
            self.draw_queen(row, col)
            if self.check_solution():
                messagebox.showinfo("8 Queens Game", "Congratulations! You won!")
        else:
            messagebox.showwarning("8 Queens Game", "Invalid placement. Try again.")

    def on_queen_click(self, event):
        """Initiate drag for the selected queen."""
        self.drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_queen_drag(self, event):
        """Update the position of the dragged queen."""
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.drag_data["item"], dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_queen_drop(self, event):
        """Place the queen in the new position."""
        item = self.drag_data["item"]
        self.drag_data["item"] = None
        coords = self.canvas.coords(item)
        col = (coords[0] + self.queen_size / 2) // self.cell_size
        row = (coords[1] + self.queen_size / 2) // self.cell_size
        row = int(row)
        col = int(col)
        self.update_board_with_queen(row, col)
        self.setup_board()
        self.draw_queen(row, col)
        if self.check_solution():
            messagebox.showinfo("8 Queens Game", "Congratulations! You won!")

    def update_board_with_queen(self, row, col):
        """Update the board with the queen's new position."""
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.board[row][col] = 1

    def get_grid_coords(self, x, y):
        """Get the grid coordinates from canvas coordinates."""
        row = int(y // self.cell_size)
        col = int(x // self.cell_size)
        return row, col

    def is_valid_placement(self, row, col):
        """Check if placing a queen at the specified position is valid."""
        # Check column and diagonals
        for r in range(self.board_size):
            if self.board[r][col] == 1:
                return False
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False
        for r, c in zip(range(row, -1, -1), range(col, self.board_size)):
            if self.board[r][c] == 1:
                return False
        return True

    def check_solution(self):
        """Check if the current board configuration is a solution."""
        queens = [(r, c) for r in range(self.board_size) for c in range(self.board_size) if self.board[r][c] == 1]
        if len(queens) != 8:
            return False
        for row1, col1 in queens:
            for row2, col2 in queens:
                if (row1, col1) != (row2, col2):
                    if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                        return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = EightQueensGame(root)
    root.mainloop()
