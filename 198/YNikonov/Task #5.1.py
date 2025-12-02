import heapq  # 5.1 ЕГЭ

N, M, K, C = map(int, input().split())
cities = list(map(int, input().split()))
arrM = []
for i in range(M):
    arrM.append(input().split())


class w_graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w, directed=False):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = w
        if not directed:
            self.graph[v][u] = w

    def deijkstra(self, start):
        distances = {vertex: float("infinity") for vertex in self.graph}
        distances[start] = 0
        priority_q = [(0, start)]

        while priority_q:
            cur_distance, cur_vertex = heapq.heappop(priority_q)

            if cur_distance > distances[cur_vertex]:
                continue

            for neighbor, weight in self.graph[cur_vertex].items():
                distance = cur_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_q, (distance, neighbor))

        return distances


newGraph = w_graph()
for i in range(M):
    newGraph.add_edge(arrM[i][0], arrM[i][1], int(arrM[i][2]))

distances = newGraph.deijkstra(str(C))

# Фильтруем и сортируем города
result = []
for city in cities:
    city_str = str(city)
    if city_str in distances and distances[city_str] != float("infinity"):
        result.append((city, distances[city_str]))

# Сортируем сначала по расстоянию, затем по номеру города
result.sort(key=lambda x: (x[1], x[0]))

for i in range(min(K, len(result))):
    print(result[i][0], result[i][1])
