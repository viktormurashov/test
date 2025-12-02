a = input()
open_count = 0
result = 0
for symbol in a:
    if symbol == '(':
        open_count += 1
    else:  # symbol == ')'
        if open_count > 0:
            open_count -= 1
        else:
            result += 1
result += open_count
print(result)