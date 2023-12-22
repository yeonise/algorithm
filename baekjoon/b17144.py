# 미세먼지 안녕!
import sys

R, C, T = map(int, input().split())
dusts = [[*map(int, sys.stdin.readline().split())] for _ in range(R)]

# 공기 청정기의 위치 찾기
air_cleaner = []

for i in range(R):
    if dusts[i][0] == -1:
        air_cleaner.append((i, 0))


# 미세먼지 확산
def spread():
    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]
    spread_dusts = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if dusts[i][j] > 0:
                amount = dusts[i][j] // 5

                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]

                    if 0 <= nr < R and 0 <= nc < C:
                        if (nr, nc) not in air_cleaner:
                            spread_dusts[nr][nc] += amount
                            dusts[i][j] -= amount

    for i in range(R):
        for j in range(C):
            dusts[i][j] += spread_dusts[i][j]


# 공기 청정기 작동
def clean():
    # 위쪽 바람은 반시계 방향으로 순환
    row = air_cleaner[0][0]
    temp = 0
    for col in range(1, C):  # 왼쪽에서 오른쪽
        dusts[row][col], temp = temp, dusts[row][col]

    for r in range(row - 1, -1, -1):  # 아래에서 위
        dusts[r][C - 1], temp = temp, dusts[r][C - 1]

    for col in range(C - 2, -1, -1):  # 오른쪽에서 왼쪽
        dusts[0][col], temp = temp, dusts[0][col]

    for r in range(1, row):  # 위에서 아래
        dusts[r][0], temp = temp, dusts[r][0]

    # 아래쪽 바람은 시계 방향으로 순환
    row = air_cleaner[1][0]
    temp = 0
    for col in range(1, C):  # 왼쪽에서 오른쪽
        dusts[row][col], temp = temp, dusts[row][col]

    for r in range(row + 1, R):  # 위에서 아래
        dusts[r][C - 1], temp = temp, dusts[r][C - 1]

    for col in range(C - 2, -1, -1):  # 오른쪽에서 왼쪽
        dusts[R - 1][col], temp = temp, dusts[R - 1][col]

    for r in range(R - 2, row, -1):  # 아래에서 위
        dusts[r][0], temp = temp, dusts[r][0]


for _ in range(T):
    spread()
    clean()

print(sum(map(sum, dusts)) + 2)
