N, M = 3, 2
roads = [
    (1, 2, 1),
    (2, 3, 2)
]
graph = [[] for _ in range(N + 1)]
for u, v, w in roads:
    graph[u].append((v, w))
    graph[v].append((u, w))
max_dists = [0] * (N + 1)
for start in range(1, N + 1):
    dist = [-1] * (N + 1)
    dist[start] = 0
    queue = [start]
    for u in queue:
        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                queue.append(v)
    max_dists[start] = max(dist[1:])
best = 1
for i in range(2, N + 1):
    if max_dists[i] < max_dists[best]:
        best = i
print(best)