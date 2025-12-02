a = int(input())
numbers = list(map(int, input().split()))
result = [-1] * a
stack = []
for b in range(a):
    current = numbers[b]
    while stack and current < numbers[stack[-1]]:
        prev_index = stack.pop()
        result[prev_index] = current 
    stack.append(b)
output = ""
for b in range(a):
    output += str(result[b]) + " "
print(output.strip())