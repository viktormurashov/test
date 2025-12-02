# Задача 1.1 - Bubble Sort
def bubble_sort(num):
    n = len(num)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                swapped = True
        if not swapped:
            break
    return num

# Задача 1.2 - Merge Sort
def merge_sort(tree):
    if len(tree) <= 1:
        return tree
    mid = len(tree) // 2
    left_half = merge_sort(tree[:mid])
    right_half = merge_sort(tree[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

# Задача 1.3 - Quick Sort
def quick_sort(num):
    if len(num) <= 1:
        return num
    opora = num[len(num) // 2]
    less = [x for x in num if x < opora]
    equal = [x for x in num if x == opora]
    greater = [x for x in num if x > opora]
    return quick_sort(less) + equal + quick_sort(greater)




