# 풍선 터뜨리기
from collections import deque

N = int(input())
papers = map(int, input().split())
orders = deque([])

for index, paper in enumerate(papers):
    orders.append((index + 1, paper))

answer = []

count = 0
while orders:
    if count > 0:
        for _ in range(abs(count) - 1):
            orders.append(orders.popleft())
    else:
        for _ in range(abs(count)):
            orders.appendleft(orders.pop())

    order, direction = orders.popleft()
    answer.append(order)
    count = direction

print(*answer)
