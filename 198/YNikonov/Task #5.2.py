# 5.2 Развиваем инфраструктуру
INF = 10**9
N, M = map(int, input().split())

# Матрица расстояний
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0

# Чтение рёбер
for _ in range(M):
    u, v, w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)
    dist[v][u] = min(dist[v][u], w)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][k] < INF and dist[k][j] < INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

eccentricity = [0] * (N + 1)
min_ecc = INF
best_vertex = -1

for i in range(1, N + 1):
    ecc = 0
    for j in range(1, N + 1):
        if dist[i][j] < INF:
            ecc = max(ecc, dist[i][j])
        else:
            ecc = INF
            break
    eccentricity[i] = ecc
    if ecc < min_ecc or (ecc == min_ecc and i < best_vertex):
        min_ecc = ecc
        best_vertex = i

print(best_vertex)
