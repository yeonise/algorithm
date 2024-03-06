# 괄호
import sys


def is_valid_ps(string):
    stack = []

    for parenthesis in string:
        if not stack and parenthesis == ')':
            return 'NO'
        elif parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'

    return 'YES' if not stack else 'NO'


T = int(sys.stdin.readline())

for _ in range(T):
    print(is_valid_ps(sys.stdin.readline()))
