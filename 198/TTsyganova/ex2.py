S = input().strip()
T = input().strip()

def cyclic_shift(S, T):
    if len(S) != len(T):
        return -1
    
    SS = S + S
    pos = SS.find(T)
    
    if pos == -1:
        return -1

    shift = (len(S) - pos) % len(S)
    return shift

print(cyclic_shift(S, T))