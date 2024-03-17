# 데이터 체커
import sys

read = sys.stdin.readline
N = int(read())
points = []
for i in range(N):
    x, r = map(int, read().split())
    points.append((x - r, i))
    points.append((x + r, i))
points.sort()

stack = []
for p in points:
    if stack and stack[-1][1] == p[1]:
        stack.pop()
    else:
        stack.append(p)

print("YES" if not stack else "NO")
