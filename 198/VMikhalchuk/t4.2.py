n = input().split()
arr = [int(x) for x in n]
res = []


class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TNode(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TNode(value)
            else:
                self._add(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TNode(value)
            else:
                self._add(node.right, value)

    def OneSubNode(self, node, res):
        if node is None:
            return

        has_left = node.left is not None
        has_right = node.right is not None

        if has_left != has_right:
            res.append(node.value)
        self.OneSubNode(node.left, res)
        self.OneSubNode(node.right, res)

    def is_balanced(self):
        if self._check_balance(self.root) != 1:
            print("yes")
            return "yes"
        else:
            print("no")
            return "no"

    def _check_balance(self, node):
        if node is None:
            return 0
        left_h = self._check_balance(node.left)
        if left_h == -1:
            return -1
        right_h = self._check_balance(node.right)
        if left_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1


newTree = BST()
for i in arr:
    if i == 0:
        break
    newTree.add(i)
newTree.OneSubNode(newTree.root, res)
res.sort()
for val in res:
    print(val)
newTree.is_balanced()
