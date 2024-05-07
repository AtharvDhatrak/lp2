def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def kruskal(nodes, edges):
    result = []  # This will store the resultant MST
    i, e = 0, 0  # Initialize count of edges and index variable
    edges = sorted(edges, key=lambda item: item[2])  # Sort edges based on weight
    parent, rank = [], []
    for node in range(nodes):
        parent.append(node)
        rank.append(0)
    while e < nodes - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result

def prim(nodes, edges):
    adj = {i: [] for i in range(nodes)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * nodes
    result = []
    # Arbitrarily choose the start node as 0
    edge_list = [(0, 0, 0)]  # (weight, from_node, to_node)
    while edge_list:
        w, u, v = min(edge_list, key=lambda item: item[0])
        edge_list.remove((w, u, v))
        if not visited[v]:
            visited[v] = True
            result.append((u, v, w))
            for next_node, weight in adj[v]:
                if not visited[next_node]:
                    edge_list.append((weight, v, next_node))
    return result[1:]  # Exclude the initial dummy edge

def dijkstra(nodes, edges, start):
    adj = {i: [] for i in range(nodes)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    dist = [float('inf')] * nodes
    dist[start] = 0
    visited = [False] * nodes
    for _ in range(nodes):
        u = min((i for i in range(nodes) if not visited[i]), key=lambda x: dist[x], default=-1)
        if u == -1:
            break
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist
