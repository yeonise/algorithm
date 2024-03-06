# 요세푸스 문제
from collections import deque

N, K = map(int, input().split())

queue = deque([str(i) for i in range(1, N + 1)])
answer = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())

    answer.append(queue.popleft())

print("<" + ", ".join(answer) + ">")
