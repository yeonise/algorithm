# 이동하기
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
table = [list(map(int, read().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1] = table[0][0]

dr = [1, 1, 0]
dc = [0, 1, 1]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        for i in range(3):
            nr = r - dr[i]
            nc = c - dc[i]

            if 0 <= nr <= N and 0 <= nc <= M:
                dp[r][c] = max(dp[nr][nc] + table[r - 1][c - 1], dp[r][c])

print(dp[-1][-1])
