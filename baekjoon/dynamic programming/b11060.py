# 접프 점프
N = int(input())
jumps = list(map(int, input().split()))

dp = [float('inf')] * (N + 1)
dp[1] = 0

for i in range(1, N + 1):
    count = jumps[i - 1]

    for j in range(1, count + 1):
        if i + j <= N:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

print(dp[-1] if dp[-1] < float('inf') else -1)
