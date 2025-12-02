#Ветки двоичного дерева
nums = list(map(int, input().split()))[:-1]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Строю дерево
root = None
for num in nums:
    if not root:
        root = Node(num)
        continue
    curr = root
    while curr:
        if num < curr.val:
            if not curr.left:
                curr.left = Node(num)
                break
            curr = curr.left
        else:
            if not curr.right:
                curr.right = Node(num)
                break
            curr = curr.right

# Ищу вершины с одним ребенком
res = []
stack = [root]
while stack:
    node = stack.pop()
    
    # Проверяю: только левый или только правый
    if (node.left and not node.right) or (not node.left and node.right):
        res.append(node.val)
    
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)

print(*sorted(res))

#Сбалансировано ли дерево?
nums = list(map(int, input().split()))[:-1]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Строю дерево
root = None
for num in nums:
    if not root:
        root = Node(num)
    else:
        curr = root
        while curr:
            if num < curr.val:
                if not curr.left:
                    curr.left = Node(num)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(num)
                    break
                curr = curr.right

# Проверяю баланс
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def balanced(node):
    if not node:
        return True
    return abs(height(node.left) - height(node.right)) <= 1 and \
           balanced(node.left) and balanced(node.right)

print("YES" if balanced(root) else "NO")