# Задача 2.1 - Поиск подстроки
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

# Задача 2.2 - Циклический сдвиг
def find_cyclic_shift(s, t):
    if len(s) != len(t):
        return -1
    
    # если строки одинаковые, сдвиг 0
    if s == t:
        return 0
    
    # создаем удвоенную строку S 
    double_s = s + s
    
    # ищем вхождение T в строке S
    index = double_s.find(t)
    
    if index != -1:
        # минимальный сдвиг вправо = длина строки - индекс
        return len(s) - index
    else:
        return -1

# проверка данных 
# if __name__ == "__main__":
#     s = input().strip()
#     t = input().strip()
#     
#     result = find_cyclic_shift(s, t)
#     print(result)
