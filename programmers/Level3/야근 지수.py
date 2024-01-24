from collections import Counter
from heapq import heapify, heappop, heappush


def solution(n, works):
    counter = Counter(works)
    works = list(map(lambda x: x * - 1, works))
    heapify(works)
    finished = 0

    while works and finished < n:
        current_work = heappop(works) * -1
        if counter[current_work] > 0:
            counter[current_work] -= 1

            updated_work = current_work - 1
            if updated_work > 0:
                if updated_work in counter:
                    counter[updated_work] += 1
                else:
                    counter[updated_work] = 1
                heappush(works, updated_work * -1)

            finished += 1

    answer = 0
    for key, value in counter.items():
        answer += (key ** 2) * value

    return answer
