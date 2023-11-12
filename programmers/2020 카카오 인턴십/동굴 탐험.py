from collections import deque


def solution(n, path, order):
    graph = [[] for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    key = [0] * n
    lock = [0] * n

    for a, b in order:
        key[a] = b
        lock[b] = a

    visited = [False] * n

    ##########

    queue = deque([0])
    revisits = set()

    while queue:
        current = queue.popleft()

        if lock[current] != 0:  # 잠겨있는 방을 방문했다면 다시 방문할 목록에 기록하기
            revisits.add(current)
            continue

        visited[current] = True

        if key[current] != 0:  # key가 되는 방을 방문했으므로 이어진 다음 방 열기
            lock[key[current]] = 0

            if key[current] in revisits:  # 잠겨있는 방을 먼저 방문했는지 확인하기
                queue.append(key[current])
                revisits.remove(key[current])

        for child in graph[current]:
            if not visited[child]:
                queue.append(child)

    return sum(visited) == n
