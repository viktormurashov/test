# Задача 2.1 - Поиск подстроки
S = input().strip()
T = input().strip()

if not T:
    print("")
else:
    result = []
    start = 0
    
    while True:
        pos = S.find(T, start)
        
        if pos == -1:
            break
            
        result.append(pos)
        
        start = pos + 1
    
    print(' '.join(map(str, result)))

# Задача 2.2 - Циклический сдвиг
# S = input().strip()
# T = input().strip()
# 
# if len(S) != len(T):
#     print(-1)
# else: 
#     for shift in range(len(S)):
#         match = True
#         for i in range(len(S)):
#             if S[(i - shift) % len(S)] != T[i]:
#                 match = False
#                 break
#         
#         if match:
#             print(shift)
#             break
#     else:
#         print(-1)




