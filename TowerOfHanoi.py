import tkinter as tk
from tkinter import messagebox
import random

class TowerOfHanoi(tk.Frame):
    def __init__(self, master, num_disks):
        super().__init__(master)
        self.master = master
        self.pack()

        self.colors = ['yellow', 'red', 'blue', 'pink', 'cyan', 'magenta', 'green', 'orange', 'light gray']
        random.shuffle(self.colors)
        
        self.num_disks = num_disks
        self.rods = [[], [], []]
        self.disk_colors = [[], [], []]
        self.selected_disk = None
        self.selected_rod = -1
        self.top_color = None

        self.create_widgets()
        self.init_disks(num_disks)

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=600, height=400, bg='black')
        self.canvas.pack()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.select_disk_btns = [
            tk.Button(self.button_frame, text=f"Select Disk from Rod {i + 1}", command=lambda i=i: self.select_disk(i))
            for i in range(3)
        ]
        for i, btn in enumerate(self.select_disk_btns):
            btn.grid(row=0, column=i, padx=5)

        self.move_to_rod_btns = [
            tk.Button(self.button_frame, text=f"Move to Rod {i + 1}", command=lambda i=i: self.move_to_rod(i))
            for i in range(3)
        ]
        for i, btn in enumerate(self.move_to_rod_btns):
            btn.grid(row=1, column=i, padx=5)

    def init_disks(self, val):
        self.rods = [[], [], []]
        self.disk_colors = [[], [], []]

        for i in range(val):
            x = 600 / 6
            width = val * 25 - 20 * i
            height = 20
            y = 400 - (i + 1) * height - 20  # Adjust y-coordinate for correct placement
            rect = (x - width / 2, y, x + width / 2, y + height)
            self.rods[0].append((rect, width))
            self.disk_colors[0].append(self.colors[i])

        self.selected_disk = None
        self.selected_rod = -1
        self.top_color = None
        self.draw_disks()

    def select_disk(self, rod_index):
        if self.rods[rod_index]:
            self.selected_disk, self.disk_width = self.rods[rod_index].pop()
            self.top_color = self.disk_colors[rod_index].pop()
            self.selected_rod = rod_index
            self.draw_disks()

    def move_to_rod(self, rod_index):
        if self.selected_disk:
            y = 400 - 20 if not self.rods[rod_index] else self.rods[rod_index][-1][0][1] - 20
            x = int(600 / 6 + (600 / 3) * rod_index)
            self.selected_disk = (x - self.disk_width / 2, y, x + self.disk_width / 2, y + 20)
            self.rods[rod_index].append((self.selected_disk, self.disk_width))
            self.disk_colors[rod_index].append(self.top_color)
            self.selected_disk = None
            self.selected_rod = -1
            self.top_color = None
            self.draw_disks()
            if len(self.rods[2]) == self.num_disks:
                messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def draw_rods(self):
        holder_x = 600 / 6
        holder_y1 = 400 - 10 * 20
        holder_y2 = 400 - 20

        self.canvas.create_line(holder_x, holder_y1, holder_x, holder_y2, fill="white", width=5)
        self.canvas.create_line(3 * holder_x, holder_y1, 3 * holder_x, holder_y2, fill="white", width=5)
        self.canvas.create_line(5 * holder_x, holder_y1, 5 * holder_x, holder_y2, fill="white", width=5)
        self.canvas.create_line(0, holder_y2, 600, holder_y2, fill="white", width=5)

    def draw_disks(self):
        self.canvas.delete("all")
        self.draw_rods()
        for rod in range(3):
            for i, (disk, width) in enumerate(self.rods[rod]):
                self.canvas.create_rectangle(disk, fill=self.disk_colors[rod][i], outline='black')
        if self.selected_disk:
            self.canvas.create_rectangle(self.selected_disk, fill=self.top_color, outline='black')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tower of Hanoi")
    game = TowerOfHanoi(root, 4)
    root.mainloop()
