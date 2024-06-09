# 오타
sequence = input()
stack = []

prefix_sum = [[0, 0] for _ in range(len(sequence))]

if sequence[0] == '(':
    prefix_sum[0] = [1, 0]
else:
    prefix_sum[0] = [0, 1]

for index in range(1, len(sequence)):
    if sequence[index] == '(':
        prefix_sum[index] = [prefix_sum[index - 1][0] + 1, prefix_sum[index - 1][1]]
    else:
        prefix_sum[index] = [prefix_sum[index - 1][0], prefix_sum[index - 1][1] + 1]

for index, char in enumerate(sequence):
    if char == '(':
        stack.append((index, char))
    elif char == ')' and stack and stack[-1][1] == '(':
        stack.pop()
    else:
        stack.append((index, char))

answer = 0

if not stack:
    print(answer)
else:
    if stack[0][1] == ')':
        answer += prefix_sum[stack[0][0]][1]
    else:
        answer += prefix_sum[-1][0] - prefix_sum[stack[-1][0] - 1][0]

    print(answer)
