x = list(input())

stack = []
result = 0
value = 1
for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])
        value *= 2

    elif x[i] == '[':
        stack.append(x[i])
        value *= 3

    elif x[i] == ')':
        if not stack or stack[-1] == '[': #스택이 없거나, 쌍괄호가 아니면 break
            result = 0
            break
        if x[i-1] == '(': # 연달아서 등장하는 올바른 쌍괄호라면 value값을 result에 추가 & value값을 이전 값으로 되돌림 
            result += value
        #올바른 쌍괄호지만 연달아서 등장하지 않는 경우, value 값을 이전 값으로 되돌리는 것만 수행
        stack.pop()
        value //= 2

    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if x[i-1] == '[':
            result += value
        stack.pop()
        value //= 3
        
if stack:
    print(0)
else:
    print(result)