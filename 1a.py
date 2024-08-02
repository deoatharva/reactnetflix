import tkinter as tk
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        self.traversal.append(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.traversal = []
        self.DFSUtil(v, visited)
        return self.traversal

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DFS Traversal Visualization")

        self.g = Graph()
        self.g.addEdge(0, 1)
        self.g.addEdge(0, 2)
        self.g.addEdge(1, 2)
        self.g.addEdge(2, 0)
        self.g.addEdge(2, 3)
        self.g.addEdge(3, 3)

        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()

        self.result_label = tk.Label(master, text="DFS Traversal: ")
        self.result_label.pack()

        self.dfs_button = tk.Button(master, text="Run DFS", command=self.run_dfs)
        self.dfs_button.pack()

        self.node_positions = [(100, 100), (250, 50), (250, 150), (400, 100)]
        self.node_radius = 20
        self.node_items = []

        self.draw_graph()

    def draw_graph(self):
        # Draw nodes
        for idx, (x, y) in enumerate(self.node_positions):
            node = self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                           x + self.node_radius, y + self.node_radius,
                                           outline='black', fill='white')
            self.node_items.append(node)
            self.canvas.create_text(x, y, text=str(idx), font=("Arial", 14, "bold"))

        # Draw edges
        for u in self.g.graph:
            for v in self.g.graph[u]:
                self.canvas.create_line(*self.node_positions[u], *self.node_positions[v], fill='black')

    def run_dfs(self):
        traversal = self.g.DFS(2)
        self.result_label.config(text="DFS Traversal: " + " -> ".join(map(str, traversal)))
        self.animate_dfs(traversal)

    def animate_dfs(self, traversal):
        def animate_step(index):
            if index < len(traversal):
                current_node = traversal[index]
                self.canvas.itemconfig(self.node_items[current_node], fill='yellow')  # Highlight visited node
                self.master.after(1000, lambda: animate_step(index + 1))  # Delay for visualization

        animate_step(0)

def main():
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
