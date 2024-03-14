# 탑

N = int(input())
heights = list(map(int, input().split()))
stack = [(1, heights[0])]
answer = [0]

for i in range(1, len(heights)):
    top = heights[i]

    while stack and stack[-1][1] < top:
        stack.pop()

    if not stack:
        answer.append(0)
    elif stack[-1][1] >= top:
        answer.append(stack[-1][0])

    stack.append((i + 1, top))

print(*answer)
