#Получение ПСП
s = input().strip() # "))))((((()()"

count = 0
result = 0

for char in s:
    if char == '(':
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            result += 1

result += count
print(result)

#Ближайший меньший

n = int(input())

arr = list(map(int, input().split()))

result = [-1] * n

for i in range(n):
    found = False
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            result[i] = j
            found = True
            break

print(' '.join(map(str, result)))