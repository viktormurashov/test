a = input().split()
p = [int(f) for f in a]               # перевод в массив 
res = []
class Tnode:                          # узел дерева
    def __init__(self, val):
        self.val = val                # значение узла
        self.left = None              # левый потомок
        self.right = None             # правый потомок
class bintree:
    def __init__(self):
        self.root = None              # корень дерева    
    def add(self, val):
        if self.root is None:
            self.root = Tnode(val)    # создаем корень, если дерево пустое
        else:
            self._add(self.root, val) # рекурсивно добавляем в нужное место

    def _add(self, node, val):
        if val < node.val:            # Если значение меньше текущего узла, идем в левое поддерево
            if node.left is None:
                node.left = Tnode(val) # создаем новый узел слева
            else:
                self._add(node.left, val) # продолжаем поиск в левом поддереве

        elif val > node.val:              # Если значение больше текущего узла, идем в правое поддерево
            if node.right is None:
                node.right = Tnode(val)   # создаем новый узел справа
            else:
                self._add(node.right, val) # продолжаем поиск в правом поддереве
        

    def onesubnode(self, node, res):
        if node is None:
            return
        hs_left = node.left is not None    # есть ли левый потомок?
        hs_right = node.right is not None  # есть ли правый потомок?

        if hs_left != hs_right :
            res.append(node.val)

        self.onesubnode(node.left, res)
        self.onesubnode(node.right, res)

newT = bintree()
for i in p:
    if i == 0:
        break
    newT.add(i)

newT.onesubnode(newT.root, res)

res.sort()                                 # сортируем значения по возрастанию
for vl in res:
    print(vl)









        

      






