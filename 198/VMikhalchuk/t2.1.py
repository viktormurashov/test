str1 = input()
str2 = input()
w = []
i = 0
while i < len(str1) + 1 - len(str2):
    index = str1.find(str2, i)
    if index == -1:
        break
    w.append(index)
    i = index + 1
print(w)
