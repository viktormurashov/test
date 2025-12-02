n = int(input())
str = input().split()
a = [int(g) for g in str]  # из букв в циферы
f = [-1] * n  # делаем массив из -1 с длинной n
stack = []
for i in range(n):
    while stack and a[i] < a[stack[-1]]:
        f[stack.pop()] = i
    stack.append(i)
print(f)
