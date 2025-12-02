a = input()
b = input()
if len(a) != len(b):
    print(-1)
else:
    n = len(a)
    result = -1
    for i in range(n):
        new_str = a[n-i:] + a[:n-i]
        if new_str == b:
            result = i
            break
    print(result)