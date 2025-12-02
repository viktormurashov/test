def occurrences(pattern, text):
    indices = []
    pattern_len = len(pattern)
    
    for i in range(len(text) - pattern_len + 1):
        found = True
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            indices.append(i)
    
    return indices

text = "ababbababa"
pattern = "aba"
result = occurrences(pattern, text)
print(result)