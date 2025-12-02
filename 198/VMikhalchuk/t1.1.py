def b(x):
    if len(x) <= 1:
        return x

    for k in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]

    return x


ea = [1, 7, 2, 5, 9, 9, 8, 6, 4, 6, 3, 5, 2, 3, 4]
print(b(ea))
