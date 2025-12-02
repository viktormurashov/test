numbers = [int(x) for x in input().split()]
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    base = lst[len(lst) // 2]
    left = [x for x in lst if x < base]
    middle = [x for x in lst if x == base]
    right = [x for x in lst if x > base]
    return quick_sort(left) + middle + quick_sort(right)
initial = numbers.copy()
sorted_numbers = quick_sort(numbers)
print("Начальные данные:", initial)
print("Сортировка:", sorted_numbers)

