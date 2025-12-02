s = input()
a = 0 # сколько удалить
o = 0 # открытые
for c in s:
    if c =="(":
        o += 1
    else:
        if o > 0 :
            o -= 1
        else:
            a += 1
a += o
print(a)
        