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

def check_balanced(root):
    if root is None:
        return 0 
    
    # проверяем левое и правое поддеревья
    left_height = check_balanced(root.left)
    right_height = check_balanced(root.right)
    
    # если какое-то поддерево не сбалансировано, возвращаем -1
    if left_height == -1 or right_height == -1:
        return -1
    
    # проверяем разницу высот
    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

def is_balanced(root):
    return check_balanced(root) != -1

def main():
    # чтение данных
    numbers = list(map(int, input().split()))
    
    # бираем 0
    numbers = [x for x in numbers if x != 0]
    
    if not numbers:
        print("YES")
        return
    
    # построение дерева
    root = None
    for num in numbers:
        root = insert_node(root, num)
    
    if is_balanced(root):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()