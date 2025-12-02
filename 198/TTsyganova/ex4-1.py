import sys
sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def collect_one_child(root, res):
    if root is None:
        return
    left = root.left is not None
    right = root.right is not None
    if left ^ right:    
        res.append(root.val)
    collect_one_child(root.left, res)
    collect_one_child(root.right, res)



nums = list(map(int, input().split()))
root = None
for x in nums:
    if x == 0:
        break
    root = insert(root, x)

ans = []
collect_one_child(root, ans)
ans.sort()

print(*ans)