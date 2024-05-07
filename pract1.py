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

    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def recursive_bfs(self, queue, visited):
        if not queue:
            return  # No more nodes to process, end recursion
        current_level_nodes = queue
        queue = []
        for node in current_level_nodes:
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        self.recursive_bfs(queue, visited)  # Process the next level

    def bfs(self, start):
        visited = set()
        self.recursive_bfs([start], visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)
print("\nBFS starting from vertex 2 using simulated recursion:")
g.bfs(3)
