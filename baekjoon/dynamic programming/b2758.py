# 로또
import sys

read = sys.stdin.readline

T = int(read())

# 1 ≤ n ≤ 10
# 1 ≤ m ≤ 2,000
# n ≤ m
for _ in range(T):
    N, M = map(int, read().split())
    # 1개만 골랐을 경우
    # 2개까지 골랐을 경우
    # 3개까지 골랐을 경우
    # 4개까지 골랐을 경우 => 답

    dp = [[0] * (M + 1) for _ in range(N)]
    for i in range(1, M + 1):  # 숫자 1개만 골랐을 경우
        dp[0][i] = i

    for i in range(1, N):  # 숫자 2개 ~ N개 골랐을 경우
        for number in range(i, M + 1):
            dp[i][number] += dp[i - 1][number // 2] + dp[i][number - 1]

    print(dp[N - 1][-1])
