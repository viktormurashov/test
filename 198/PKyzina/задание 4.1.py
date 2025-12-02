s = input("Введите последовательность целых чисел, оканчивающаяся нулем").split()
d = []
i = 0
while i < len(s) and s[i] != '0':
    d.append(int(s[i]))
    i += 1
class N:
    def __init__(self, v):
        self.v = v          
        self.l = None       
        self.r = None        
def a(r, x):
    if not r: return N(x)
    if x < r.v: r.l = a(r.l, x)
    elif x > r.v: r.r = a(r.r, x)
    return r
def f(r):
    if not r: return []
    res = []
    if (r.l is None) != (r.r is None):
        res.append(r.v)
    return res + f(r.l) + f(r.r)
r = None
for x in d:
    r = a(r, x)
res = f(r)
res.sort()
print(*res)
