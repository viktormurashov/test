example = '())(()'
count = 0
flag = False
for char in example:
    if char == '(' in example:
        flag = True
        print(flag)
    elif char == ')' in example and flag == True:
        flag = False
        print(flag)
        count +=1
print(count)


def count_parentheses_stack(text):
    stack = []
    pair_count = 0
    
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                pair_count += 1
    return pair_count

example = "())(()"
result = count_parentheses_stack(example)
print(len(example) - result * 2)