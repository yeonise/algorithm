import sys

n = int(sys.stdin.readline())
locations = [*map(int, sys.stdin.readline().split())]

min_gap = 1_000_000
answer = 0

for index in range(1, n):
    gap = locations[index] - locations[index - 1]

    if gap < min_gap:
        min_gap = gap
        answer = 1
    elif gap == min_gap:
        answer += 1

print(answer)
