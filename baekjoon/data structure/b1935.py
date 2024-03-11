# 후위 표기식2
from collections import deque

def calculate(a, b, o):
    if o == '+':
        return a + b
    if o == '-':
        return a - b
    if o == '/':
        return a / b
    if o == '*':
        return a * b


N = int(input())
string = input()
mapper = {}
start = ord('A')

for i in range(N):
    mapper[chr(start + i)] = input()

problem = deque([])

for char in string:
    if char in mapper:
        problem.append(mapper[char])
    else:
        problem.append(char)

stack = []

while len(stack) > 1 or problem:
    popped = problem.popleft()

    if popped.isdigit():
        stack.append(int(popped))
    else:
        number1 = stack.pop()
        number2 = stack.pop()
        stack.append(calculate(number2, number1, popped))

print(format(stack[0], ".2f"))
