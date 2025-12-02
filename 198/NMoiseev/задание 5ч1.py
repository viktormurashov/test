N, M, K, C = 5, 4, 5, 1
cities = [1, 2, 3, 4, 5]
roads = [
    (1, 2, 1),
    (2, 3, 10), 
    (3, 4, 100),
    (4, 5, 100)
]
graph = [[] for _ in range(N + 1)]
for u, v, t in roads:
    graph[u].append((v, t))
    graph[v].append((u, t))
INF = 10**9
dist = [INF] * (N + 1)
dist[C] = 0
import heapq
heap = [(0, C)]
while heap:
    time, u = heapq.heappop(heap)
    if time > dist[u]:
        continue
    for v, t in graph[u]:
        new_time = time + t
        if new_time < dist[v]:
            dist[v] = new_time
            heapq.heappush(heap, (new_time, v))
results = []
for city in cities:
    results.append((city, dist[city]))
results.sort(key=lambda x: x[1])
for city, time in results:
    print(city, time)