from collections import Counter


def solution(k, tangerine):
    answer = 0
    total = 0

    counter = Counter(tangerine).values()

    for count in sorted(counter, reverse=True):
        total += count
        answer += 1

        if total >= k:
            break

    return answer
