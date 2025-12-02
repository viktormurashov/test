s = "())())()()))(())(("
balance = 0
remove_count = 0
for char in s:
    if char == '(':
        balance += 1
    else:
        if balance > 0:
            balance -= 1
        else:
            remove_count += 1
remove_count += balance
print(remove_count)