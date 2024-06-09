# 구간 합 구하기 5
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
table = [[0] * (N + 1)]

for _ in range(N):
    table.append([0] + list(map(int, read().split())))

for row in range(1, N + 1):
    for col in range(1, N + 1):
        table[row][col] += table[row][col - 1]

for col in range(1, N + 1):
    for row in range(1, N + 1):
        table[row][col] += table[row - 1][col]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())

    print(table[x2][y2] - table[x2][y1 - 1] - table[x1 - 1][y2] + table[x1 - 1][y1 - 1])
