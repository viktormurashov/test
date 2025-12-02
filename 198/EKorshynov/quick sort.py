num = [8, 4, 1, 3, 2, 5, 7, 6]  #список чисел

def quick_sort(num):    
    if len(num) <= 1:   #если в списке 0 или 1 число, то он готов
        return num

    pivot = num[0]  #выбираем первое число из списка как опорное pivot

    left = []   #пустой список для чисел, которые <= pivot
    right = []  #пустой список для чисел, которые > pivot

    for x in num[1:]:   #перебираем все числа из списка, кроме 1
        if x <= pivot:  #если число меньше или равно pivot
            left.append(x) #добавляем его в левый список
        else:
            right.append(x) #добавляем его в правый список

    return quick_sort(left) + [pivot] + quick_sort(right) #отсортированная левая часть+pivot+отсортированная правая часть

print(quick_sort(num))
