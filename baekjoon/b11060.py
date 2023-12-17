# 점프 점프
import collections

N = int(input())

if N == 1:
    print(0)
    exit()

numbers = [*map(int, input().split())]

dp = [1001] * N
queue = collections.deque([(0, 0)])  # 현재 위치 인덱스, 정수, 현재 점프 수

while queue:
    index, jump = queue.popleft()

    for i in range(1, numbers[index] + 1):
        if index + i < N and dp[index + i] > jump + 1:
            dp[index + i] = jump + 1
            queue.append((index + i, jump + 1))

print(dp[-1] if dp[-1] != 1001 else -1)
