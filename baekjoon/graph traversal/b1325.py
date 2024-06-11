# 효율적인 해킹
import sys
from collections import defaultdict, deque

read = sys.stdin.readline

N, M = map(int, read().split())  # N: 총 컴퓨터 수 M: 신뢰 관계 수

graph = defaultdict(list)
for _ in range(M):  # 그래프를 생성하는 시간 복잡도 : O(M)
    A, B = map(int, read().split())
    graph[B].append(A)

hack_count_list = [0] * (N + 1)


def bfs(start):
    visited = [0] * (N + 1)
    visited[start] = 1
    queue = deque([start])
    count = 1

    while queue:
        node = queue.popleft()
        hack_count_list[node] += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
                count += 1

    return count


max_hack = 0
result = []

for computer in range(1, N + 1):
    hack_count = bfs(computer)

    if max_hack < hack_count:
        result = [computer]
        max_hack = hack_count
    elif max_hack == hack_count:
        result.append(computer)

print(*result)
