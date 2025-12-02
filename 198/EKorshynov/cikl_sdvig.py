S = input() #считываем строку S
T = input() #считываем строку T

if len(S) != len(T): #если длины разные - сразу -1
    print(-1)
else:
    for step in range(len(S)): #перебираем все сдвиги вправо
        step2 = S[-step:] + S[:-step] #делаем циклический сдвиг вправо

        if step2 == T: #если совпадает с T - выводим сдвиг
            print(step)
            break
    else:
        print(-1) #если ни один сдвиг не подошёл
