import tkinter as tk
from tkinter import messagebox

class BlockWorldGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Block World Game")
        
        self.goal = ['A', 'B', 'C']  # Desired order
        self.columns = {
            'left': [],   # Column 1
            'middle': [], # Column 2
            'right': []   # Column 3
        }
        self.create_widgets()
        self.setup_game()

    def create_widgets(self):
        self.frames = {
            'left': tk.Frame(self.root, width=200, height=300, bg='lightgray', borderwidth=2, relief='ridge'),
            'middle': tk.Frame(self.root, width=200, height=300, bg='lightgray', borderwidth=2, relief='ridge'),
            'right': tk.Frame(self.root, width=200, height=300, bg='lightgray', borderwidth=2, relief='ridge')
        }
        
        self.frames['left'].grid(row=0, column=0, padx=10, pady=10)
        self.frames['middle'].grid(row=0, column=1, padx=10, pady=10)
        self.frames['right'].grid(row=0, column=2, padx=10, pady=10)
        
        self.buttons = {
            'left_to_middle': tk.Button(self.root, text="Move Left to Middle", command=self.move_left_to_middle),
            'left_to_right': tk.Button(self.root, text="Move Left to Right", command=self.move_left_to_right),
            'middle_to_left': tk.Button(self.root, text="Move Middle to Left", command=self.move_middle_to_left),
            'middle_to_right': tk.Button(self.root, text="Move Middle to Right", command=self.move_middle_to_right),
            'right_to_left': tk.Button(self.root, text="Move Right to Left", command=self.move_right_to_left),
            'right_to_middle': tk.Button(self.root, text="Move Right to Middle", command=self.move_right_to_middle)
        }
        
        self.buttons['left_to_middle'].grid(row=1, column=0, padx=10, pady=10)
        self.buttons['left_to_right'].grid(row=2, column=0, padx=10, pady=10)
        self.buttons['middle_to_left'].grid(row=1, column=1, padx=10, pady=10)
        self.buttons['middle_to_right'].grid(row=2, column=1, padx=10, pady=10)
        self.buttons['right_to_left'].grid(row=1, column=2, padx=10, pady=10)
        self.buttons['right_to_middle'].grid(row=2, column=2, padx=10, pady=10)
    
    def setup_game(self):
        # Initialize the blocks in the correct columns
        self.columns['left'] = ['A']
        self.columns['middle'] = ['B']
        self.columns['right'] = ['C']
        self.update_gui()
    
    def update_gui(self):
        # Clear all frames
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                widget.destroy()
        
        # Update frames with blocks
        for column, blocks in self.columns.items():
            frame = self.frames[column]
            for block in blocks:
                tk.Label(frame, text=block, bg='lightblue', padx=20, pady=10, relief='raised').pack(pady=10)
        
        self.check_win()
    
    def move_left_to_middle(self):
        self.move_block('left', 'middle')
    
    def move_left_to_right(self):
        self.move_block('left', 'right')
    
    def move_middle_to_left(self):
        self.move_block('middle', 'left')
    
    def move_middle_to_right(self):
        self.move_block('middle', 'right')
    
    def move_right_to_left(self):
        self.move_block('right', 'left')
    
    def move_right_to_middle(self):
        self.move_block('right', 'middle')
    
    def move_block(self, from_col, to_col):
        if self.columns[from_col]:
            block = self.columns[from_col].pop()
            self.columns[to_col].append(block)
            self.update_gui()

    def check_win(self):
        # Check if blocks are in the goal state
        if (self.columns['middle'] == ['A'] and
            self.columns['middle'] == ['B'] and
            self.columns['middle'] == ['C']):
            messagebox.showinfo("Congratulations!", "You've solved the puzzle!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockWorldGame(root)
    root.mainloop()
