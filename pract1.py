class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def bfs(self, s):
        visited = set()
        queue = [s]
        visited.add(s)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Example usage
g = Graph()
num_edges = int(input("Enter the number of edges: "))

# Loop to add edges to the graph
for i in range(num_edges):
    edge = input(f"Enter edge {i+1} in the format 'start end': ")
    start, end = map(int, edge.split())
    g.add_edge(start, end)

print("DFS starting from vertex 2:")
g.dfs(2,set())
print("\nBFS starting from vertex 2 using simulated recursion:")
g.bfs(3)