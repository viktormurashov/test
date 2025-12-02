def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] <= right[j] else right[j])
        i, j = i + (left[i] <= right[j]), j + (left[i] > right[j])
    
    return result + left[i:] + right[j:]

masiv = [1,6,9,5,6,3]
print(merge_sort(masiv))  # [1, 3, 5, 6, 6, 9]



















   