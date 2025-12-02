nums = [8, 4, 12, 2, 6, 10, 14, 0]
nums = nums[:-1]
result = []
n = len(nums)
for i in range(n):
    left_kid = None
    right_kid = None
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            left_kid = nums[j]
            break
    for j in range(i+1, n):
        if nums[j] > nums[i]:
            right_kid = nums[j]
            break
    kids = 0
    if left_kid:
        kids += 1
    if right_kid:
        kids += 1
    if kids == 1:
        result.append(nums[i])
result.sort()
print(' '.join(map(str, result)))