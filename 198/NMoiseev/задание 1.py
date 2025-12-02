n = [5, 2, 8, 1, 9, 3]

#баблсортировка
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print(n)

# Быстрая сортировка (Quick Sort)
def qs(arr):
    # Базовый случай: массив из 0 или 1 элемента
    if len(arr) <= 1:
        return arr
    p = arr[len(arr)//2]  # Выбираем опорный элемент (pivot)
    left = [x for x in arr if x < p]
    mid = [x for x in arr if x == p]
    right = [x for x in arr if x > p]
    return qs(left) + mid + qs(right)

# ---------- Комментарии и рекомендации по улучшению ----------

# 1. Эта реализация быстрой сортировки проста и работает корректно, 
#    но она не "in-place" — на каждом уровне рекурсии создаются новые массивы left, mid и right.
#    При больших объемах данных это увеличивает использование памяти.

# 2. Улучшение — реализовать быструю сортировку на месте (in-place), что не будет требовать дополнительной памяти под массивы.
#    Обычно это делается с помощью двух указателей и вспомогательной функции partition.

# 3. Также имеет смысл для массовых одинаковых элементов (или почти отсортированных массивов) выбрать случайный опорный элемент (randomized quicksort),
#    чтобы уменьшить шанс худшего случая O(n^2).

# Пример улучшенной реализации (in-place QuickSort):

def quicksort_inplace(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort_inplace(arr, low, p - 1)
        quicksort_inplace(arr, p + 1, high)

def partition(arr, low, high):
    # Можно улучшить и выбирать случайный опорный элемент для устойчивости к худшим случаям
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Проверка работы улучшенной быстрой сортировки:
arr = [5, 2, 8, 1, 9, 3]
quicksort_inplace(arr, 0, len(arr)-1)
print(arr) # Вывод отсортированного массива
