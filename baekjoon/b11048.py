# 이동하기
row, column = map(int, input().split())

candy = [[*map(int, input().split())] for _ in range(row)]
record = [[0] * column for _ in range(row)]

for i in range(0, row):
    for j in range(0, column):
        record[i][j] = max(record[i - 1][j], record[i][j - 1]) + candy[i][j]

print(record[row - 1][column - 1])
