import collections
import re


def solution(expression):
    groups = [
        ["*", "+", "-"],
        ["+", "-", "*"],
        ["-", "*", "+"],
        ["*", "-", "+"],
        ["+", "*", "-"],
        ["-", "+", "*"],
    ]

    def calculate(o, a, b):
        if o == "+":
            return str(int(a) + int(b))
        if o == "*":
            return str(int(a) * int(b))
        if o == "-":
            return str(int(a) - int(b))

    answer = 0

    splited = re.findall(r'\d+|[-+*/]', expression)

    for group in groups:
        arr = collections.deque(splited)
        stack = []

        for op in group:
            while arr:
                if arr[0].isdigit():
                    stack.append(arr.popleft())
                elif arr[0] == op:
                    arr.popleft()
                    stack.append(calculate(op, stack.pop(), arr.popleft()))
                else:
                    stack.append(arr.popleft())

            arr = collections.deque(stack)
            stack = []

        answer = max(answer, abs(int(arr.pop())))

    return answer
