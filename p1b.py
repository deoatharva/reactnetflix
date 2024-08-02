import tkinter as tk
from collections import deque

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("BFS Traversal of a Graph")
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()

        # Number of vertices in the graph
        self.vertices = 5

        # Adjacency list representation of the graph
        self.adjList = [[] for _ in range(self.vertices)]

        # Add edges to the graph
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(1, 3)
        self.addEdge(3, 2)
        self.addEdge(2, 4)

        # Button to start BFS traversal
        self.traversal_button = tk.Button(master, text="Start BFS Traversal", command=self.start_bfs)
        self.traversal_button.pack()

        # Canvas coordinates for drawing nodes
        self.node_positions = [(100, 100), (250, 50), (250, 150), (400, 50), (400, 150)]
        self.node_radius = 20
        self.node_items = []

    def addEdge(self, u, v):
        self.adjList[u].append(v)

    def draw_graph(self):
        # Draw nodes
        for idx, (x, y) in enumerate(self.node_positions):
            node = self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                           x + self.node_radius, y + self.node_radius,
                                           outline='black', fill='white')
            self.node_items.append(node)
            self.canvas.create_text(x, y, text=str(idx), font=("Arial", 14, "bold"))

        # Draw edges
        for u in range(self.vertices):
            for v in self.adjList[u]:
                self.canvas.create_line(*self.node_positions[u], *self.node_positions[v], fill='black')

    def start_bfs(self):
        # Mark all the vertices as not visited
        visited = [False] * self.vertices

        # Perform BFS traversal starting from vertex 0
        self.bfs(0, visited)

    def bfs(self, startNode, visited):
        # Create a queue for BFS
        q = deque()

        # Mark the current node as visited and enqueue it
        visited[startNode] = True
        q.append(startNode)

        # Function to animate BFS traversal
        def animate_bfs():
            if q:
                currentNode = q.popleft()
                self.canvas.itemconfig(self.node_items[currentNode], fill='yellow')  # Highlight visited node

                for neighbor in self.adjList[currentNode]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

                self.master.after(1000, animate_bfs)  # Delay for visualization

        animate_bfs()

# Create the main window
root = tk.Tk()
app = GraphGUI(root)
app.draw_graph()
root.mainloop()
