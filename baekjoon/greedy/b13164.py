# 행복 유치원
import sys

read = sys.stdin.readline
N, K = map(int, read().split())
heights = list(map(int, read().split()))

gaps = []
for index, height in enumerate(heights):
    if index + 1 == len(heights):
        break

    gaps.append(heights[index + 1] - height)

gaps.sort()

for _ in range(K - 1):
    gaps.pop()

print(sum(gaps))
