s = input().strip()

stack = 0
remove = 0

for ch in s:
    if ch == '(':
        stack += 1
    else:  # ')'
        if stack > 0:
            stack -= 1
        else:
            remove += 1


print(remove + stack)