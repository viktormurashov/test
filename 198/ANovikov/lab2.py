
def kmp_prefix_function(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp_search(text, pattern):
    pi = kmp_prefix_function(pattern)
    j = 0
    results = []
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            results.append(i - j + 1)
            j = pi[j-1]
    return results

def cyclic_shift(S, T):
    if len(S) != len(T):
        return -1
    doubled = S + S
    pos = doubled.find(T)
    if pos == -1:
        return -1
    # минимальный сдвиг вправо
    return (len(S) - pos) % len(S)

if __name__ == "__main__":
    # Задача 1
    S = input().strip()
    T = input().strip()
    occurrences = kmp_search(S, T)
    print(*occurrences)

    # Переход к задаче 2 (можно запускать отдельно)
    # Для теста можно раскомментировать следующий блок:

    # S = input().strip()
    # T = input().strip()
    # print(cyclic_shift(S, T))
