# 말이 되고픈 원숭이
import sys
from collections import deque

read = sys.stdin.readline

K = int(read())
W, H = map(int, read().split())
land = [list(map(int, read().split())) for _ in range(H)]

hr = [-1, -2, -2, -1, 1, 2, 2, 1]
hc = [-2, -1, 1, 2, -2, -1, 1, 2]
mr = [0, -1, 0, 1]
mc = [-1, 0, 1, 0]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
queue = deque([(0, 0, K)])

while queue:
    row, col, k = queue.popleft()
    count = visited[row][col][k]

    if row == H - 1 and col == W - 1:
        print(visited[-1][-1][k])
        exit()

    for i in range(4):
        nr = row + mr[i]
        nc = col + mc[i]

        if 0 <= nr < H and 0 <= nc < W and not land[nr][nc] and not visited[nr][nc][k]:
            queue.append((nr, nc, k))
            visited[nr][nc][k] = count + 1

    if k > 0:
        for i in range(8):
            nr = row + hr[i]
            nc = col + hc[i]

            if 0 <= nr < H and 0 <= nc < W and not land[nr][nc] and not visited[nr][nc][k - 1]:
                queue.append((nr, nc, k - 1))
                visited[nr][nc][k - 1] = count + 1

print(-1)
