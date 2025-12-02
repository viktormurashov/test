def test_example():
    s = "ababbababa"
    t = "aba"
    result = kmp_search(s, t)
    print(f"значения: S='{s}', T='{t}'")
    print(f"Результат: {result}")

def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(s, t):
    n = len(s)
    m = len(t)
    if m == 0:
        return []
    lps = build_lps(t)
    indices = []
    i = j = 0
    while i < n:
        if t[j] == s[i]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and t[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    result = kmp_search(s, t)
    print(" ".join(map(str, result)))



test_example()