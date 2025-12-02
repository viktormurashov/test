# Задача 3.1 - Получение ПСП
def PSP(s):
    midle = 0
    delite = 0
    for ch in s:
        if ch == '(':
            midle += 1
        elif ch == ')':
            if midle > 0:
                midle -= 1
            else:
                delite += 1
    delite += midle
    return delite

# Задача 3.2 - Ближайший меньший
from typing import List

def naersmall(nums: List[int]) -> List[int]:
    ind = []
    result = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while ind and nums[ind[-1]] >= nums[i]:
            ind.pop()
        if ind:
            result[i] = nums[ind[-1]]
        ind.append(i)
    return result

if __name__ == "__main__":
    # Задача 3.1
    s1 = input().strip()
    print(PSP(s1))
    
    # Задача 3.2
    # nums = list(map(int, input().strip().split()))
    # result = naersmall(nums)
    # print(' '.join(map(str, result)))




