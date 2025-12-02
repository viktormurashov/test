str = input()
r = 0
o = 0
for s in str:
    if s == "(":
        o += 1
    else:
        if o > 0:
            o -= 1
        else:
            r += 1
r += o
print(r)
