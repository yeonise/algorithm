# 죽음의 비
import sys
from collections import deque

read = sys.stdin.readline

N, H, D = map(int, read().split())  # 길이 N, 체력 H, 내구도 D
land = [list(read().strip()) for _ in range(N)]

start = None
for i in range(N):
    flag = False
    for j in range(N):
        if land[i][j] == 'S':
            start = [i, j, H, 0, 0]
            flag = True
            break
    if flag:
        break

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque([start])
visited = [[-1] * N for _ in range(N)]
visited[start[0]][start[1]] = H

while queue:
    row, col, health, umbrella, count = queue.popleft()

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if land[nr][nc] == 'E':
                print(count + 1)
                exit()

            next_health = health
            next_umbrella = umbrella

            if land[nr][nc] == 'U':
                next_umbrella = D

            if next_umbrella == 0:
                next_health -= 1
            else:
                next_umbrella -= 1

            if next_health > 0 and visited[nr][nc] < next_umbrella + next_health:
                visited[nr][nc] = next_umbrella + next_health
                queue.append([nr, nc, next_health, next_umbrella, count + 1])

print(-1)
