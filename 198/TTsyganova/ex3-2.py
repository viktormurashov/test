n = int(input().strip())
arr = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] >= arr[i]:
        stack.pop()
    result[i] = stack[-1] if stack else -1
    stack.append(arr[i])

print(*result)