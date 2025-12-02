#Поиск подстроки
s = input().strip()  # "aabbaabbbaab"
t = input().strip()  # "aab"

# Поиск вхождений
result = []
for i in range(len(s) - len(t) + 1):
    # Проверяю кусок строки s длиной t
    if s[i:i+len(t)] == t:
        result.append(i)

# Вывод результата
print(' '.join(map(str, result)))  


#Циклический сдвиг
s = input().strip()  # "zadcb"
t = input().strip()  # "adcbz"

# Проверка длин
if len(s) != len(t):
    print(-1)
else:
    # Проверяю все возможные сдвиги
    found = -1
    for shift in range(len(s)):
        # Создаю циклический сдвиг
        shifted = s[-shift:] + s[:-shift]
        if shifted == t:
            found = shift
            break
    print(found)