# 블로그
import sys

read = sys.stdin.readline

N, X = map(int, read().split())
views = list(map(int, read().split()))

if X == 1:
    print(max(views))
    exit()

left = 0
right = 0
current = 0
max_views = 0
count = 0

while right < X:
    current += views[right]
    right += 1

if current > 0:
    max_views = current
    count += 1

while right < N:
    current += views[right]
    current -= views[left]
    right += 1
    left += 1

    if max_views == current:
        count += 1
    elif max_views < current:
        max_views = current
        count = 1

if max_views > 0:
    print(max_views)
    print(count)
else:
    print("SAD")
