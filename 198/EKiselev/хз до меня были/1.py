def min_removals_to_balance(s):
    balance = 0
    removals = 0
    
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            if balance > 0:
                balance -= 1
            else:
                removals += 1
    
    # в конце добавляем оставшиеся незакрытые открывающие скобки
    removals += balance
    
    return removals

# входные данные
if __name__ == "__main__":
    s = input().strip()
    result = min_removals_to_balance(s)
    print(result)