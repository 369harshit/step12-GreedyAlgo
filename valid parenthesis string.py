def checkValidString(s):
    stack = []
    asterisks = []
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == '*':
            asterisks.append(i)
        else:  # char == ')'
            if stack:
                stack.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False
            
    while stack:
        if not asterisks or stack.pop() > asterisks.pop():
            return False
    return True

input_str = "()"
print(checkValidString(input_str))  # Output: True
