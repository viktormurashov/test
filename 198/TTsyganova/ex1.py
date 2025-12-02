S = input().strip()
T = input().strip()

positions = []
i = 0
while i < len(S):
    idx = S.find(T, i)
    if idx == -1:
        break
    positions.append(idx)
    i = idx + 1 

print(' '.join(map(str, positions)) if positions else '')