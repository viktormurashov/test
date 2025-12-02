class Node:
    def __init__(self, val):
        self.val = val              # Значение узла
        self.left = None            # Левый потомок
        self.right = None           # Правый потомок

class BinTree:
    def __init__(self):
        self.root = None            # Корень дерева (изначально дерево пустое)
    
    def add(self, val):
        if self.root is None:       # Если дерево пустое, создаем корневой узел
            self.root = Node(val)
        else:                       # Иначе рекурсивно добавляем в нужное место
            self._add(self.root, val)
    
    def _add(self, node, val):      # Вспомогательный рекурсивный метод для добавления узла
        if val < node.val:          # Если значение меньше текущего узла, идем в левое поддерево
            if node.left is None:   # Если левого потомка нет, создаем новый узел
                node.left = Node(val)
            else:                   # Иначе продолжаем поиск в левом поддереве
                self._add(node.left, val)
        elif val > node.val:        # Если значение больше текущего узла, идем в правое поддерево
            if node.right is None:  # Если правого потомка нет, создаем новый узел
                node.right = Node(val)
            else:                   # Если правого потомка нет, создаем новый узел
                self._add(node.right, val)
    
    def is_balanced(self):
        return self._check_balance(self.root) != -1 # Дерево сбалансировано, если _check_balance не вернул -1
    
    def _check_balance(self, node): # Вспомогательный рекурсивный метод проверки сбалансированности
        if node is None:            # Базовый случай: пустое поддерево имеет высоту 0
            return 0
        
        left_h = self._check_balance(node.left)  # Рекурсивно вычисляем высоту левого поддерева
        if left_h == -1:             # Если левое поддерево несбалансировано, возвращаем -1
            return -1
        
        right_h = self._check_balance(node.right) # Рекурсивно вычисляем высоту правого поддерева
        if right_h == -1:            # Если правое поддерево несбалансировано, возвращаем -1
            return -1
        
        if abs(left_h - right_h) > 1:  # Проверяем разницу высот левого и правого поддеревьев
            return -1                # Дерево несбалансировано
        
        return max(left_h, right_h) + 1 # Возвращаем высоту текущего поддерева


numbers = list(map(int, input().split()))  # Чтение входных данных - последовательности чисел
tree = BinTree()                    # Создание пустого бинарного дерева

for num in numbers:                 # Построение дерева из входной последовательности
    if num == 0:
        break                       # 0 - признак конца последовательности
    tree.add(num)                   # Добавляем число в дерево

print("YES" if tree.is_balanced() else "NO") # Проверка сбалансированности и вывод результата