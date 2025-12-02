def merge_sort(h):
    if len(h) <= 1:
        return h
    seredina = len(h) // 2
    levo = merge_sort(h[:seredina])
    pravo = merge_sort(h[seredina:])
    return marge(levo, pravo)


def marge(l, p):
    vishlo = []
    i = j = 0
    while len(l) > i and len(p) > j:
        if l[i] <= p[j]:
            vishlo.append(l[i])
            i += 1
        else:
            vishlo.append(p[j])
            j += 1
    vishlo.extend(l[i:])
    vishlo.extend(p[j:])
    return vishlo


g = [1, 9, 8, 5, 8, 7, 6, 6, 3, 4, 7, 4, 7, 6, 5, 5]
print(merge_sort(g))
