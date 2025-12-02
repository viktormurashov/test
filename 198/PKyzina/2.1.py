S = input()
T = input()
result = []
a = len(S)
b = len(T)
for i in range(a - b + 1):
    if S[i:i + b] == T:
        result.append(i)
print(*result)
