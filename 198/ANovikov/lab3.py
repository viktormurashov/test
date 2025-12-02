
# Задача 1
def min_deletions_to_PSP(s):
    open_count = 0
    deletions = 0
    for ch in s:
        if ch == '(':
            open_count += 1
        else:  # ch == ')'
            if open_count > 0:
                open_count -= 1
            else:
                deletions += 1
    deletions += open_count
    return deletions

# Задача 2
def nearest_smaller_right(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

if __name__ == "__main__":
    # Тест Задачи 1
    s = input().strip()
    print(min_deletions_to_PSP(s))

    # Тест Задачи 2
    # Считываем
    n = int(input())
    arr = list(map(int, input().split()))
    res = nearest_smaller_right(arr)
    print(*res)
