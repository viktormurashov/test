# ЕГЭ
N, M, K, C = map(int, input().split())
cities = list(map(int, input().split()))

# Граф
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    graph[v].append((u, t))

# Поиск кратчайших путей
dist = [10**9] * (N + 1)
dist[C] = 0
queue = [C]

for node in queue:
    for neighbor, t in graph[node]:
        new_time = dist[node] + t
        if new_time < dist[neighbor]:
            dist[neighbor] = new_time
            queue.append(neighbor)

# Вывод результатов
result = []
for city in cities:
    result.append((dist[city], city))

result.sort()

for time, city in result:
    print(city, time)


# Развиваем инфраструктуру
N, M = map(int, input().split())

# Матрица расстояний
dist = [[10**9] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

# Дороги
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = w
    dist[v][u] = w

# Поиск кратчайших путей
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# Площадка с минимальным максимальным расстоянием
best = 1
min_max = 10**9

for i in range(N):
    curr_max = max(dist[i])
    if curr_max < min_max:
        min_max = curr_max
        best = i + 1

print(best)