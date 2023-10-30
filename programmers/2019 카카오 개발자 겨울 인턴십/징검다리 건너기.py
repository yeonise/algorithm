import collections


def solution(stones, k):
    answer = 300_000_000
    max_queue = collections.deque()

    for i in range(k):
        while max_queue and stones[max_queue[-1]] < stones[i]:
            max_queue.pop()

        max_queue.append(i)

    answer = min(answer, stones[max_queue[0]])

    for i in range(k, len(stones)):
        while max_queue and stones[max_queue[-1]] < stones[i]:
            max_queue.pop()

        max_queue.append(i)

        if max_queue and max_queue[0] <= i - k:
            max_queue.popleft()

        answer = min(answer, stones[max_queue[0]])

    return answer
