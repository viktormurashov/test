def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index - 1)
            _quick_sort(items, split_index + 1, high)
    def partition(items, low, high):
        pivot = items[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while items[i] < pivot:
                i += 1
            j -= 1
            while items[j] > pivot:
                j -= 1
            if i >= j:
                return j
            items[i], items[j] = items[j], items[i]
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


numbers_list = [100, 358, 5, 14, 1544, 11, 90, 55, 234, 6]
print("список чисел до сортировки:", numbers_list)
quick_sort(numbers_list)
print("список чисел после сортировки:", numbers_list)