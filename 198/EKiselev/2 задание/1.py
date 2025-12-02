def find_all_occurrences(s, t):
    indices = []
    pattern_length = len(t)
    text_length = len(s)
    
    # проходим по всем возможным начальным позициям
    for i in range(text_length - pattern_length + 1):
        # проверяем, совпадает ли подстрока с шаблоном
        if s[i:i + pattern_length] == t:
            indices.append(i)
    
    return indices

# чтение данных
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    
    # находим все вхождения
    result = find_all_occurrences(s, t)
    
    # выводим результат 
    print(' '.join(map(str, result)))