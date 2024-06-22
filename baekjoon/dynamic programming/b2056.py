# 작업
import sys

read = sys.stdin.readline

N = int(read())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    info = list(map(int, read().split()))
    time = info[0]
    max_previous = 0

    for previous in info[2:]:
        max_previous = max(max_previous, dp[previous])

    dp[i] = max_previous + time

print(max(dp))
