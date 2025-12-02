import heapq
import sys

input = sys.stdin.readline


N, M, K, C = map(int, input().split())
cities = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    graph[v].append((u, t))


INF = 10**18
dist = [INF] * (N + 1)
dist[C] = 0

pq = [(0, C)] 

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for to, w in graph[node]:
        nd = d + w
        if nd < dist[to]:
            dist[to] = nd
            heapq.heappush(pq, (nd, to))


result = []
for city in cities:
    result.append((dist[city], city))


result.sort()


for t, city in result:
    print(city, t)