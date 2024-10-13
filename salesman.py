import tkinter as tk
import numpy as np
from itertools import permutations

class TSPGame:
    def __init__(self, master):
        self.master = master
        master.title("Traveling Salesman Problem Game")

        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack()

        self.cities = []
        self.city_entries = []

        self.input_frame = tk.Frame(master)
        self.input_frame.pack()

        self.city_label = tk.Label(self.input_frame, text="Enter city coordinates (x,y):")
        self.city_label.pack(side=tk.LEFT)

        self.city_entry = tk.Entry(self.input_frame)
        self.city_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.input_frame, text="Add City", command=self.add_city)
        self.add_button.pack(side=tk.LEFT)

        self.solve_button = tk.Button(master, text="Solve TSP", command=self.solve_tsp)
        self.solve_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def add_city(self):
        entry = self.city_entry.get()
        try:
            x, y = map(int, entry.split(','))
            self.cities.append((x, y))
            self.city_entry.delete(0, tk.END)
            self.draw_cities()
        except ValueError:
            print("Invalid input. Please enter coordinates as x,y.")

    def draw_cities(self):
        self.canvas.delete("all")
        for (x, y) in self.cities:
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

    def calculate_distance(self, city1, city2):
        return np.linalg.norm(np.array(city1) - np.array(city2))

    def total_distance(self, path):
        return sum(self.calculate_distance(self.cities[path[i]], self.cities[path[i - 1]]) for i in range(len(path)))

    def solve_tsp(self):
        if len(self.cities) < 2:
            print("Add at least two cities.")
            return

        best_path = None
        min_distance = float('inf')

        for perm in permutations(range(len(self.cities))):
            distance = self.total_distance(perm)
            if distance < min_distance:
                min_distance = distance
                best_path = perm

        self.draw_best_path(best_path)

    def draw_best_path(self, path):
        for i in range(len(path)):
            x1, y1 = self.cities[path[i]]
            x2, y2 = self.cities[path[(i + 1) % len(path)]]
            self.canvas.create_line(x1, y1, x2, y2, fill='red', width=2)

    def reset(self):
        self.cities = []
        self.canvas.delete("all")
        self.city_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    tsp_game = TSPGame(root)
    root.mainloop()
