import sys

sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    graph = [[] for _ in range(len(a))]

    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    # 자식 노드의 모든 가중치를 루트 노드에게 전달한다
    # 임의의 루트 노드 0

    if sum(a) != 0:
        return -1

    visited = [False] * len(a)
    visited[0] = True
    total = [0]

    def dfs(parent, node):

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                dfs(node, child)

        total[0] += abs(a[node])
        a[parent] += a[node]

    dfs(0, 0)

    return total[0]
