s = input("Введите последовательность целых чисел, оканчивающуюся нулем ").split()                             
d = []
i = 0
while i < len(s) and s[i] != '0':
    d.append(int(s[i]))
    i += 1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root
def check_balanced(node):
    if node is None:
        return (True, 0)
    left_balanced, left_height = check_balanced(node.left)
    right_balanced, right_height = check_balanced(node.right)
    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    height = 1 + max(left_height, right_height)
    return (balanced, height)
root = None
for num in d:
    root = insert(root, num)
balanced, _ = check_balanced(root)
print("YES" if balanced else "NO")
