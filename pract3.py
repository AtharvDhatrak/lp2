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

def kruskal(nodes, edges):
    result, i, e = [], 0, 0 
    edges = sorted(edges, key=lambda item: item[2]) 
    parent, rank = list(range(max(max(edge[0], edge[1]) for edge in edges) + 1)), [0] * (max(max(edge[0], edge[1]) for edge in edges) + 1)
    while e < nodes - 1:
        u, v, w = edges[i]; i += 1; x, y = find(parent, u), find(parent, v)
        if x != y: e, result = e + 1, result + [(u, v, w)]; union(parent, rank, x, y)
    return result

def prim(nodes, edges):
    max_node = max(max(edge[0], edge[1]) for edge in edges) + 1  
    adj, visited, result, edge_list = {i: [] for i in range(1, max_node)}, [False] * max_node, [], [(0, 0, 1)]
    for u, v, w in edges: adj[u].append((v, w)); adj[v].append((u, w))
    while edge_list:
        w, u, v = min(edge_list, key=lambda item: item[0]); edge_list.remove((w, u, v))
        if not visited[v]: visited[v], result = True, result + [(u, v, w)]
        for next_node, weight in adj[v]:
            if not visited[next_node]: edge_list.append((weight, v, next_node))
    return result[1:] 


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
