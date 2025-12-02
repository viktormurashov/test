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
        # минимальный сдвиг вправо = длина строки
        return len(s) - index
    else:
        return -1

# проверка данных 
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    
    result = find_cyclic_shift(s, t)
    print(result)