from collections import deque
from collections import defaultdict


def solution(n, path, order):
    visited = [False] * n
    visited[0] = True

    pathes = defaultdict(list)

    for a, b in path:
        pathes[a].append(b)
        pathes[b].append(a)

    orders = [-1] * n

    for a, b in order:
        orders[b] = a

    queue = deque([0])
    waiting_list = defaultdict(set)

    while queue:
        current = queue.popleft()

        must_visited_room = orders[current]

        if must_visited_room == -1 or visited[must_visited_room]:
            visited[current] = True

            for room in waiting_list[current]:
                queue.append(room)
        else:
            waiting_list[must_visited_room].add(current)
            continue

        for p in pathes[current]:
            if not visited[p]:
                queue.append(p)

    return True if sum(visited) == n else False


solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]])
solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]])
