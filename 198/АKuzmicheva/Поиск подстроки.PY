s = input()
t = input()
res = []
a = 0
while a < len(s):
    inx = s.find(t, a)
    if inx == -1:
        break
    res.append(inx)
    a = inx + 1
print(res)