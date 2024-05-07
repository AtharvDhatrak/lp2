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
graph = [
    [(1, 1), (3, 3)],  # Connections from node 0 to 1 with cost 1 and to 3 with cost 3
    [(1, 0), (1, 2), (4, 3)],  # Connections from node 1 to 0 with cost 1, to 2 with cost 1, and to 3 with cost 4
    [(1, 1), (2, 3)],  # Connections from node 2 to 1 with cost 1 and to 3 with cost 2
    [(3, 0), (4, 1), (2, 2)]  # Connections from node 3 to 0 with cost 3, to 1 with cost 4, and to 2 with cost 2
]

print("Prim's MST:", prims(graph, 0))
print("Kruskal's MST:", kruskals(graph))
print("Dijkstra's Shortest Paths from Node 0:", dijkstra(graph, 0))
