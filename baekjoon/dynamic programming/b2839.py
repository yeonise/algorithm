# 설탕 배달

N = int(input())

# Greedy
# if N % 5 == 0:
#     print(N // 5)
# else:
#     count = 0
#     while N > 0:
#         N -= 3
#         count += 1
#         if N % 5 == 0:
#             count += N // 5
#             print(count)
#             break
#         elif N == 0:
#             print(count)
#             break
#         elif N < 3:
#             print(-1)
#             break

# DP
if N < 3 or N == 4 or N == 7:
    print(-1)
elif N % 5 == 0:
    print(N // 5)
elif N == 3:
    print(1)
else:
    dp = [float('inf')] * (N + 1)
    dp[3] = 1
    dp[5] = 1

    for i in range(6, N + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

    print(dp[N] if dp[N] < float('inf') else -1)
