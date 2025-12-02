numbers = input().split()
numbers = [int(x) for x in numbers] 
def bubble_sort(lst):
    a = len(lst)
    for b in range(a):
        for c in range(0, a - b - 1):
            if lst[c] > lst[c + 1]:
                lst[c], lst[c + 1] = lst[c + 1], lst[c]
    return lst
initial_data = numbers.copy()
sorted_numbers = bubble_sort(numbers)
print("Начальные данные:", initial_data)
print("Сортировка:", sorted_numbers)

