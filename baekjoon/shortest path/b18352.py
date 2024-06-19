# 특정 거리의 도시 찾기
import sys
from collections import defaultdict, deque

read = sys.stdin.readline

N, M, K, X = map(int, read().split())  # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, read().split())
    graph[A].append(B)

queue = deque([(X, 0)])
visited = [False] * (N + 1)
visited[X] = True
answer = []

while queue:
    city, distance = queue.popleft()

    for neighbor in graph[city]:
        if not visited[neighbor]:
            visited[neighbor] = True

            if distance + 1 == K:
                answer.append(neighbor)
            else:
                queue.append((neighbor, distance + 1))

if not answer:
    print(-1)
else:
    answer.sort()
    print(*answer, sep='\n')
