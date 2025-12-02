def nearest_smaller_right_indices(arr):
    n = len(arr)
    result = [-1] * n 
    stack = []
    
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            result[stack.pop()] = i
        stack.append(i)
    
    return result

numbers = [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]
indices = nearest_smaller_right_indices(numbers)
print(indices)
