# 겹치는 건 싫어
import sys
from collections import defaultdict

read = sys.stdin.readline

N, K = map(int, read().split())
numbers = list(map(int, read().split()))

counter = defaultdict(int)
left = right = 0
max_length = 0

while right < N:
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    else:
        while numbers[left] != numbers[right] and left < right:
            counter[numbers[left]] -= 1
            left += 1
        counter[numbers[right]] -= 1
        left += 1

print(max_length)
