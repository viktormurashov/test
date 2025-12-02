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

def check_balance(root):
    if root is None:
        return (0, True)

    lh, ok1 = check_balance(root.left)
    rh, ok2 = check_balance(root.right)

    balanced = ok1 and ok2 and abs(lh - rh) <= 1
    return (max(lh, rh) + 1, balanced)



nums = list(map(int, input().split()))
root = None
for x in nums:
    if x == 0:
        break
    root = insert(root, x)

height, is_balanced = check_balance(root)

print("YES" if is_balanced else "NO")