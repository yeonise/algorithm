from collections import defaultdict
from collections import deque


def solution(n, roads, sources, destination):
    graph = defaultdict(list)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    time = [-1] * (n + 1)
    time[destination] = 0
    queue = deque([(destination, 0)])

    while queue:
        d, t = queue.popleft()

        for child in graph[d]:
            if time[child] == -1:
                time[child] = t + 1
                queue.append((child, t + 1))

    return [time[source] for source in sources]
