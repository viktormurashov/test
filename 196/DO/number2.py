def compute_prefix(pattern):
    n = len(pattern)
    prefix = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        else:
            j = 0
        prefix[i] = j
    return prefix

def kmp_search(text, pattern):
    n = len(pattern)
    m = len(text)
    if n == 0:
        return []
    prefix = compute_prefix(pattern)
    j = 0
    occurrences = []
    for i in range(m):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == n:
            start_index = i - n + 1
            occurrences.append(start_index)
            j = prefix[j-1]
    return occurrences

def find_cyclic_shift(S, T):
    n = len(S)
    if n != len(T):
        return -1
        
    if n == 0:
        return 0
        
    S2 = S + S
    occurrences = kmp_search(S2, T)
    indices = [i for i in occurrences if i < n]
    
    if not indices:
        return -1
    else:
        k_list = [(n - i) % n for i in indices]
        return min(k_list)

def run_task():
    test_cases = [
        ("a", "b"),
        ("zabcd", "abcdz"),
        ("denize", "enized"),
        ("kaban", "abank"),
        ("abc", "cab"),
    ]
    
    all_passed = True
    for i, (S, T) in enumerate(test_cases, 1):
        result = find_cyclic_shift(S, T)
        print(f"  Ввод: S='{S}', T='{T}'")
        print(f"   Получено: {result}")
        all_passed = False
        print()
    
    return all_passed

if __name__ == "__main__":
     run_task()