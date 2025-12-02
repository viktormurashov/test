def find_nearest_smaller_right(n, arr):
    result = [-1] * n 
    stack = []
    
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            # нашли ближайшее меньшее справа для элемента
            idx = stack.pop()
            result[idx] = arr[i]
        # добавляем текущий индекс
        stack.append(i)
    
    return result

# обработка входных данных
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    result = find_nearest_smaller_right(n, arr)
    print(' '.join(map(str, result)))