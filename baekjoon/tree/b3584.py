# 가장 가까운 공통 조상
import collections
import sys
from collections import defaultdict

read = sys.stdin.readline
T = int(read())


def solution():
    N = int(read())
    parents = [0] * (N + 1)
    tree = defaultdict(list)

    for _ in range(N - 1):
        A, B = map(int, read().split())
        parents[B] = A
        tree[A].append(B)

    root = parents[1:].index(0) + 1
    child1, child2 = map(int, read().split())
    depths = [0] * (N + 1)
    queue = collections.deque([root])

    while queue:
        parent = queue.popleft()

        for child in tree[parent]:
            depths[child] = depths[parent] + 1
            if tree[child]:
                queue.append(child)

    def LCA(a, b):
        if depths[a] < depths[b]:
            a, b = b, a
        gap = depths[a] - depths[b]

        for _ in range(gap):
            a = parents[a]

        while a != b:
            a = parents[a]
            b = parents[b]

        return a

    print(LCA(child1, child2))


for _ in range(T):
    solution()
