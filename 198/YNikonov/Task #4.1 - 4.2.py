n = input().split()
arr = [int(x) for x in n]
result = []


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinSearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add(node.right, value)

    def oneSubNode(self, node, result):
        if node is None:
            return

        has_left = node.left is not None
        has_right = node.right is not None

        # Узел имеет только одного потомка, если есть либо левый, либо правый, но не оба
        if has_left != has_right:
            result.append(node.value)

        self.oneSubNode(node.left, result)
        self.oneSubNode(node.right, result)

    def is_balanced(self):
        if self._check_balance(self.root) != -1:
            print("YES")
            return True
        else:
            print("NO")
            return False

    def _check_balance(self, node):
        if node is None:
            return 0

        left_h = self._check_balance(node.left)
        if left_h == -1:
            return -1

        right_h = self._check_balance(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return max(left_h, right_h) + 1


newTree = BinSearchTree()
for i in arr:
    if i == 0:
        break
    newTree.add(i)

newTree.oneSubNode(newTree.root, result)
result.sort()
for val in result:
    print(val)  # Задание 4.1 Вывести ветки двоичного дерева

newTree.is_balanced()  # Задание 4.2 Проверка сбалансированности дерева
