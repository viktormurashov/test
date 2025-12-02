def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # выбираем опорный элемент
    pivot = arr[len(arr) // 2]
    
    # делим на три части
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # сортируем левую и правую части
    return quick_sort(left) + middle + quick_sort(right)

# проверка
if __name__ == "__main__":
    # массивы
    test_arrays = [[38, 27, 43, 3, 9, 82, 10],]
    
    print("проверка")
    for k, arr in enumerate(test_arrays, 1):
        original = arr.copy()
        sorted_arr = quick_sort(arr)
        print(f"проверка {k}: {original} - {sorted_arr}")