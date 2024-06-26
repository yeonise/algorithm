# 공주님을 구해라!
import sys
from collections import deque

read = sys.stdin.readline

N, M, T = map(int, read().split())  # 성의 크기 N, M, 저주의 제한 시간 T
castle = [list(map(int, read().split())) for _ in range(N)]
queue = deque([(0, 0, 0)])  # N, M, 걸린 시간
answer = float('inf')
dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
sword = float('inf')

while queue:
    n, m, t = queue.popleft()

    if n == N - 1 and m == M - 1:
        answer = t
        break

    if castle[n][m] == 2:
        time = t + (N - n - 1) + (M - m - 1)

        if time <= T:
            sword = time

    for i in range(4):
        nr = n + dr[i]
        nc = m + dc[i]

        if 0 <= nr < N and 0 <= nc < M and t + 1 <= T and not visited[nr][nc] and castle[nr][nc] != 1:
            queue.append((nr, nc, t + 1))
            visited[nr][nc] = 1

print("Fail" if min(sword, answer) == float('inf') else min(sword, answer))
