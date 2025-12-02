def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left, mid, right = [], [], []
    for x in arr:
        if x < pivot: 
            left.append(x)
        elif x == pivot: 
            mid.append(x)
        else: 
            right.append(x)
    return quick(left) + mid + quick(right)

ann = [1,5,6,2]
print(quick(ann)) 