def floyd_warshall(n, graph):
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    # заполнение известными ребрами
    for u in range(1, n + 1):
        for v, w in graph[u]:
            dist[u][v] = w
    
    # алгоритм Флойда-Уоршелла
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def main():
    # анализ данных
    N, M = map(int, input().split())
    
    # построение графа 
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # находим кратчайшие пути 
    dist = floyd_warshall(N, graph)
    
    max_distances = []
    for i in range(1, N + 1):
        max_dist = 0
        for j in range(1, N + 1):
            if dist[i][j] > max_dist:
                max_dist = dist[i][j]
        max_distances.append((i, max_dist))
        
    best_site = min(max_distances, key=lambda x: (x[1], x[0]))
    
    print(best_site[0])

if __name__ == "__main__":
    main()