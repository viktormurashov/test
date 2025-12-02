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


newTree = BST()
for i in arr:
    if i == 0:
        break
    newTree.add(i)
newTree.OneSubNode(newTree.root, res)
res.sort()
for val in res:
    print(val)
