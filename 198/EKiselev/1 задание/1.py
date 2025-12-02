def bubble_sort(arr):
    n = len(arr)
    
    for k in range(n):
        
        for m in range(0, n - k - 1):
            if arr[m] > arr[m + 1]:
                # Замена элементов
                arr[m], arr[m + 1] = arr[m + 1], arr[m]
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

sorted_arr = bubble_sort(arr)

print(sorted_arr)
