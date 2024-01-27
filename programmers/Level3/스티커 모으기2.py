def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp = [[0, 0, 0, 0] for _ in range(len(sticker))]  # [선택, 미선택, 선택, 미선택]
    dp[0][0] = sticker[0]  # 첫 번째 스티커 선택
    dp[1][0] = sticker[1]  # 두 번째 스티커 선택
    dp[1][2] = sticker[1]  # 두 번째 스티커 선택

    for index in range(2, len(sticker)):
        dp[index][0] = max(dp[index - 2][0], dp[index - 2][1], dp[index - 1][1]) + sticker[index]
        dp[index][1] = max(dp[index - 2][0], dp[index - 2][1], dp[index - 1][0], dp[index - 1][1])
        dp[index][2] = max(dp[index - 2][2], dp[index - 2][3], dp[index - 1][3]) + sticker[index]
        dp[index][3] = max(dp[index - 2][2], dp[index - 2][3], dp[index - 1][2], dp[index - 1][3])

    return max(dp[-1][1], dp[-1][2], dp[-1][3])
