def solution(n, tops):
    # [겹치는 타일을 사용하지 않은 경우, 겹치는 타일을 사용한 경우]
    mod = 10007

    dp = [[0, 0] for _ in range(n)]
    dp[0] = [2, 1] if tops[0] == 0 else [3, 1]

    for i in range(1, n):
        if tops[i] == 0:
            dp[i] = [(dp[i - 1][0] * 2 + dp[i - 1][1]) % mod,
                     (dp[i - 1][0] + dp[i - 1][1]) % mod]
        else:
            dp[i] = [(dp[i - 1][0] * 3 + dp[i - 1][1] * 2) % mod,
                     (dp[i - 1][0] + dp[i - 1][1]) % mod]

    return sum(dp[-1]) % mod
