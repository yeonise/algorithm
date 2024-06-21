# 줄 세우기
import sys

read = sys.stdin.readline

N = int(read())
children = [int(read()) for _ in range(N)]
dp = [1] * N

for i in range(N):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
