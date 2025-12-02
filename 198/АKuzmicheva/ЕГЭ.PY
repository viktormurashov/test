import heapq
N, M, K, C = map(int, input().split())
cities = list(map(int, input().split()))
am = []                                    # список для хранения данных о дорогах
for i in range(M):
    am.append(input().split())              # каждая дорога: [Ui, Vi, Ti]


class w_graph:
    def __init__(self):
        self.graph = {}                   # Словарь для хранения графа

    def add_edge(self, u, v, w, directed=False):  # Добавление ребра в граф
        if u not in self.graph:                   # Создаем записи для вершин, если их еще нет
            self.graph[u] = {}
        if v not in self.graph:                   # Создаем записи для вершин, если их еще нет
            self.graph[v] = {}

        self.graph[u][v] = w                      # Добавляем ребро из u в v с весом w
        if not directed:                          # если граф неориентированный, добавляем обратное ребро
            self.graph[v][u] = w

    def deijkstra(self, start):                   # Алгоритм Дейкстры для поиска кратчайших путей из начальной вершины
        distances = {vertex: float("infinity") for vertex in self.graph}
        distances[start] = 0                      # расстояние до стартовой вершины = 0
        priority_q = [(0, start)]                 # Очередь с приоритетом: (расстояние, вершина)

        while priority_q:                         
            cur_distance, cur_vertex = heapq.heappop(priority_q) # Извлекаем вершину с наименьшим расстоянием

            if cur_distance > distances[cur_vertex]:    # Если есть более короткий путь через другую вершину, пропускаем
                continue

            for neighbor, weight in self.graph[cur_vertex].items():  # Обход всех соседей текущей вершин
                distance = cur_distance + weight
                if distance < distances[neighbor]:             # Если найден более короткий путь до соседа
                    distances[neighbor] = distance
                    heapq.heappush(priority_q, (distance, neighbor))

        return distances


newGraph = w_graph()                               # Создаем граф и добавляем все дороги
for i in range(M):
    newGraph.add_edge(am[i][0], am[i][1], int(am[i][2]))

distances = newGraph.deijkstra(str(C))

result = []                                         # Формирование результата для городов
for city in cities:
    city_str = str(city)
    if city_str in distances and distances[city_str] != float("infinity"):     # Проверяем, что город достижим из столицы
        result.append((city, distances[city_str]))

result.sort(key=lambda x: (x[1], x[0]))            # Сортировка результата: сначала по времени прибытия, затем по номеру города

for i in range(min(K, len(result))):               # Вывод K пар (номер города, время прибытия)
    print(result[i][0], result[i][1])




