# 도둑
import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N, M, K = map(int, read().split())
    houses = list(map(int, read().split()))

    if N == M:
        if sum(houses) < K:
            print(1)
        else:
            print(0)
        continue

    houses.extend(houses)

    answer = 0
    left = 0
    money = sum(houses[left:left + M])

    if money < K:
        answer += 1

    while left + 1 < N:
        money -= houses[left]
        left += 1
        money += houses[left + M - 1]

        if money < K:
            answer += 1

    print(answer)
