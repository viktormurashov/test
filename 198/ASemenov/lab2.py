# Задача 2.1 - Поиск подстроки
def find_substring_indexes(S, T):
    indexes = []
    start_pos = 0
    while True:
        pos = S.find(T, start_pos)
        if pos == -1:
            break
        indexes.append(pos)
        start_pos = pos + 1
    return indexes

# Задача 2.2 - Циклический сдвиг
def min_shift(S, T):
    if len(S) != len(T):
        return -1
    
    double_S = S + S
    idx = double_S.find(T)
    if idx == -1:
        return -1
    else:
        return idx % len(S)

if __name__ == "__main__":
    # Задача 2.1
    S = input().strip()
    T = input().strip()
    indexes = find_substring_indexes(S, T)
    print(' '.join(map(str, indexes)))
    
    # Задача 2.2
    # S = input().strip()
    # T = input().strip()
    # shift = min_shift(S, T)
    # print(shift)




