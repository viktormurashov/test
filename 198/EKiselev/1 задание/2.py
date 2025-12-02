def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # разделяем массив
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # соединяем отсортированные половины
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    k = m = 0
    
    # Сравниваем элементы из обоих массивов
    while k < len(left) and m < len(right):
        if left[k] <= right[m]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[m])
            m += 1
    
    # Добавляем остатки
    result.extend(left[k:])
    result.extend(right[m:])
    
    return result

# Проверка
if __name__ == "__main__":
    # массивы
    test_arrays = [[38, 27, 43, 3, 9, 82, 10],]
    
    print("Проверка")
    for k, arr in enumerate(test_arrays, 1):
        original = arr.copy()
        sorted_arr = merge_sort(arr)
        print(f"проверка {k}: {original} - {sorted_arr}")