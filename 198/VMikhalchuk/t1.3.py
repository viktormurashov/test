def bistro(x):
    if len(x) <= 1:
        return x
    pivot = x[len(x) // 2]
    l = [i for i in x if i < pivot]
    m = [i for i in x if i == pivot]
    r = [i for i in x if i > pivot]
    return bistro(l) + m + bistro(r)


g = [1, 9, 8, 5, 8, 7, 6, 6, 3, 4, 7, 4, 7, 6, 5, 5]
print(bistro(g))
