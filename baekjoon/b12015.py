# 가장 긴 증가하는 부분 수열 2

# LIS Longest increasing Subsequence
# DP
# n = 8
# arr = [6, 2, 5, 1, 7, 4, 8, 3]
# dp = [1] * n
#
# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# O(n^2)

# 이분 탐색을 활용하여 시간 복잡도 개선
# n = 8
# arr = [6, 2, 5, 1, 7, 4, 8, 3]
# memorization = [6]
#
# for number in arr:
#     if memorization[-1] < number:
#         memorization.append(number)
#     else:
#         left = 0
#         right = len(memorization)
#
#         while left < right:
#             mid = (left + right) // 2
#
#             if memorization[mid] < number:
#                 left = mid + 1
#             else:
#                 right = mid
#
#         memorization[right] = number
# O(n log n)

n = int(input())
numbers = [*map(int, input().split())]
memorization = [numbers[0]]

for number in numbers:
    if memorization[-1] < number:
        memorization.append(number)
    else:
        left = 0
        right = len(memorization)

        while left < right:
            mid = (left + right) // 2

            if memorization[mid] < number:
                left = mid + 1
            else:
                right = mid

        memorization[right] = number

print(len(memorization))
