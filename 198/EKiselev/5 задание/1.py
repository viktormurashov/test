import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if current_dist > dist[u]:
            continue
            
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    return dist

def main():
    # анлиз входных данных
    N, M, K, C = map(int, input().split())
    cities = list(map(int, input().split()))
    
    # построение графа
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
        graph[v].append((u, t))
    
    # находим кратчайшие пути 
    dist_from_capital = dijkstra(N, graph, C)
    
    # собираем пары 
    results = []
    for city in cities:
        time = dist_from_capital[city]
        results.append((city, time))
    
    # сортируем
    results.sort(key=lambda x: x[1])
    
    # вывод 
    for city, time in results:
        print(city, time)

if __name__ == "__main__":
    main()