# 데스 나이트
import collections

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

N = int(input())
start_r, start_c, end_r, end_c = map(int, input().split())

queue = collections.deque([(start_r, start_c, 0)])
visited = [[False] * N for _ in range(N)]
visited[start_r][start_c] = True

while queue:
    r, c, count = queue.popleft()

    if r == end_r and c == end_c:
        print(count)
        exit()

    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, count + 1))

print(-1)
