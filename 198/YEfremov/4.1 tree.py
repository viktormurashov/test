class Node:
    def __init__(self, num):
        self.number = num
        self.left = None
        self.right = None
    
    def add_to_list(self, num):
        if num < self.number:
            if self.left:
                self.left.add_to_list(num)
            else:
                self.left = Node(num)
        else:
            if self.right:
                self.right.add_to_list(num)
            else:
                self.right = Node(num)

def seek(treeNode):
    res = []
    
    if (treeNode.left is None and treeNode.right is not None) or \
       (treeNode.left is not None and treeNode.right is None):
        res.append(treeNode.number)
    
    if treeNode.left:
        res.extend(seek(treeNode.left))
    if treeNode.right:
        res.extend(seek(treeNode.right))
    
    return res

data = [7, 3, 2, 1, 9, 5, 4, 6, 8]

tree = None
for i in range(len(data)):
    if not tree:
        tree = Node(data[i])
    else:
        tree.add_to_list(data[i])

result = seek(tree)
print(result)