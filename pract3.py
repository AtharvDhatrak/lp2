class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def prims(graph, start):
    import heapq
    mst = []
    visited = [False] * len(graph)
    min_heap = [(0, start, start)]  # (cost, to_node, from_node)
    
    while min_heap:
        cost, u, frm = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append((frm, u, cost))
        
        for cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (cost, v, u))
    
    return mst[1:]  # Exclude the dummy edge from start to start

def kruskals(graph):
    edges = []
    for u in range(len(graph)):
        for cost, v in graph[u]:
            edges.append((cost, u, v))
    edges.sort()
    
    uf = UnionFind(len(graph))
    mst = []
    
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))
            if len(mst) == len(graph) - 1:
                break

    return mst

def dijkstra(graph, start):
    import heapq
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    min_heap = [(0, start)]
    
    while min_heap:
        current_distance, u = heapq.heappop(min_heap)
        
        if current_distance > distances[u]:
            continue
        
        for weight, v in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))
    
    return distances

# Example usage
def edge_input_to_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    graph = [[] for _ in range(num_vertices)]

    print("Enter edges in the format 'u v w' (space-separated), where u and v are vertices and w is the cost:")
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))  # Assuming undirected graph

    return graph

# Example usage
graph = edge_input_to_graph()

print("Graph Edges and Weights:")
seen = set()
for idx, connections in enumerate(graph):
    for weight, neighbor in connections:
        if (idx, neighbor) not in seen and (neighbor, idx) not in seen:
            print(f"Edge from Node {idx} to Node {neighbor} with weight {weight}")
            seen.add((idx, neighbor))


print("Prim's MST:", prims(graph, 0))
print("Kruskal's MST:", kruskals(graph))
print("Dijkstra's Shortest Paths from Node 0:", dijkstra(graph, 0))
