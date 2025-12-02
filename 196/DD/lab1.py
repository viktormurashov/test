# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        # КРИТИЧЕСКИЙ МОМЕНТ (производительность):
        # Внутренний цикл всегда идет до len(arr)-1, даже когда "хвост" уже отсортирован.
        # Обычно здесь делают range(len(arr) - i - 1), чтобы не проверять уже отсортированные элементы.
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    # КРИТИЧЕСКИЙ МОМЕНТ (производительность):
    # pop(0) у списка - это O(n) операция, так как все элементы сдвигаются.
    # В цикле это дает O(n^2) только на слияние, вместо ожидаемого O(n log n) для merge sort.
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # КРИТИЧЕСКИЙ МОМЕНТ (ошибка корректности):
    # Элементы, равные pivot, полностью игнорируются (кроме самого pivot),
    # т.к. мы берем только < pivot и > pivot.
    # В результате теряются дубликаты!
    # Пример: quick_sort([2, 2, 2]) -> [2], ожидается [2, 2, 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [2, 2, 2]

print("Массив:", nums)
print("Bubble Sort:", bubble_sort(nums))
print("Merge Sort:", merge_sort(nums))
print("Quick Sort:", quick_sort(nums))