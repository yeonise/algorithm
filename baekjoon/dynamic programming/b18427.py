# 함께 블록 쌓기
import sys

read = sys.stdin.readline

N, M, H = map(int, read().split())  # 학생 수, 학생마다 최대 M개의 블록, 탑의 높이
dp = [[1] + [0] * H for i in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = dp[i - 1].copy()
    blocks = list(map(int, read().split()))

    for block in blocks:
        for j in range(block, H + 1):
            dp[i][j] += dp[i - 1][j - block]

print(dp[N][H] % 10007)
