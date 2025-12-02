
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers_list = [100, 358, 5, 14, 1544, 11, 90, 55, 234, 6]
print("список чисел до сортировки:", numbers_list)
bubble_sort(numbers_list)
print("список чисел после сортировки:", numbers_list)