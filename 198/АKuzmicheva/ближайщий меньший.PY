n = int(input())                              # количество элементов в массиве
p = list(map(int, input().split()))           # массив чисел
res = [-1] * n
stack = []                                    # Стек для хранения индексов элементов
for i in range(n):                            # Проход по всем элементам массива
    while stack and p[i] < p[stack[-1]]:      # Пока стек не пуст и текущий элемент меньше элемента на вершине стека
        res[stack.pop()] = i
    stack.append(i)
print(*res)