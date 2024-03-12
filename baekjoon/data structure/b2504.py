# 괄호의 값

string = input()
stack = []
answer = 0
temp = 1

for i, p in enumerate(string):
    if p == '(':
        stack.append(p)
        temp *= 2
    elif p == '[':
        stack.append(p)
        temp *= 3
    elif p == ')':
        if not stack or stack[-1] != '(':
            stack.append(p)
            break

        if string[i - 1] == '(':
            answer += temp

        stack.pop()
        temp //= 2
    elif p == ']':
        if not stack or stack[-1] != '[':
            stack.append(p)
            break

        if string[i - 1] == '[':
            answer += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
    exit()

print(answer)
