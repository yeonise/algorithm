# 괄호 제거
from itertools import combinations

origin = input()
pairs = []
stack = []

for i, char in enumerate(origin):
    if char == '(':
        stack.append((i, char))
    elif char == ')':
        pairs.append((stack.pop()[0], i))

answer = set()

for j in range(1, len(pairs) + 1):
    result = [*combinations(pairs, j)]

    for group in result:

        indexes = []
        for index in [*group]:
            indexes.append(index[0])
            indexes.append(index[1])

        temp = ''
        for i, char in enumerate(origin):
            if i not in indexes:
                temp = temp + char

        answer.add(temp)

answer = list(answer)
answer.sort()

print(*answer, sep='\n')
