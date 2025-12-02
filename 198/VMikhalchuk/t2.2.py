str1 = input()
str2 = input()
if len(str1) != len(str2):
    ptint(-1)
elif str1 == str2:
    print(0)
else:
    str1_2 = str1 + str1
    if str1_2.find(str2) != -1:
        print(len(str1) - str1_2.find(str2))
    else:
        ptint(-1)
