nums = [5, 3, 8, 2, 4, 7, 9, 0]
nums = nums[:-1]
def высота(list):
    if not list:
        return 0
    корень = list[0]
    left = [x for x in list if x < корень]
    right = [x for x in list if x > корень]
    return 1 + max(высота(left), высота(right))
def проверить(list):
    if not list:
        return True
    корень = list[0]
    left = [x for x in list if x < корень]
    right = [x for x in list if x > корень]
    lh = высота(left)
    rh = высота(right) 
    if abs(lh - rh) > 1:
        return False
    return проверить(left) and проверить(right)
if проверить(nums):
    print("YES")
else:
    print("NO")