# 배
import sys

read = sys.stdin.readline
N = int(read())
limits = list(map(int, read().split()))
M = int(read())
weights = list(map(int, read().split()))

limits.sort(reverse=True)
weights.sort()

if weights[-1] > limits[0]:
    print(-1)
    exit()

time = 0
boxes = []

while weights:

    for limit in limits:
        if not weights:
            break

        if limit >= weights[-1]:
            weights.pop()
        else:
            while weights and limit < weights[-1]:
                boxes.append(weights.pop())

            if weights:
                weights.pop()

    weights.extend(boxes)
    weights.sort()
    boxes.clear()
    time += 1

print(time)
