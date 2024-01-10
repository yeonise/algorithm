# 후위 표기식

infix = input()

operator = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}

result = []
stack = []

for char in infix:
    if char.isalpha():
        result.append(char)
    elif char == "(":
        stack.append(char)
    elif char == ")":
        while stack[-1] != "(":
            result.append(stack.pop())
        stack.pop()
    elif not stack or operator[stack[-1]] < operator[char]:
        stack.append(char)
    else:
        while stack and operator[stack[-1]] >= operator[char]:
            result.append(stack.pop())
        stack.append(char)

while stack:
    result.append(stack.pop())

print("".join(result))
