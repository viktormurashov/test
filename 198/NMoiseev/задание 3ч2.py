arr = [7, 3, 1, 0, 4, 5, 2]
n = len(arr)
result = [-1] * n
stack = []
for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        pos = stack.pop()
        result[pos] = arr[i]
    stack.append(i)
print(' '.join(map(str, result)))7