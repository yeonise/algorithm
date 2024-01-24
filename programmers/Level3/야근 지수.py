from heapq import heapify, heappop, heappush


def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-work for work in works]
    heapify(works)

    for _ in range(n):
        work = heappop(works)
        heappush(works, work + 1)

    return sum([work ** 2 for work in works])
