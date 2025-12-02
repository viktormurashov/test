class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    
    return root

def find_single_child_nodes(root, result):
    if root is None:
        return
    
    # проверяем количество детей
    has_left = root.left is not None
    has_right = root.right is not None
    
    # если только один ребенок
    if has_left != has_right: 
        result.append(root.value)
    
    find_single_child_nodes(root.left, result)
    find_single_child_nodes(root.right, result)

def main():
    # проверка входных данных
    numbers = list(map(int, input().split()))
    
    # убираем 0
    numbers = [x for x in numbers if x != 0]
    
    if not numbers:
        return
    
    # остроение дерева
    root = None
    for num in numbers:
        root = insert_node(root, num)
    
    # поиск вершин 
    result = []
    find_single_child_nodes(root, result)
    
    # сортировка 
    result.sort()
    
    # вывод 
    for value in result:
        print(value)

if __name__ == "__main__":
    main()