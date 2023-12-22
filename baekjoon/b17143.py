# 낚시왕

import sys

R, C, M = map(int, sys.stdin.readline().split())

if M == 0:
    print(0)
    exit()

sharks = [[[]] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks[r - 1][c - 1] = [d, s, z]  # 이동 방향, 속력, 크기


def fishing(column):
    # 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다
    for i in range(R):
        if sharks[i][column]:
            size = sharks[i][column][2]
            sharks[i][column].clear()

            return size

    return 0


def swim():
    global sharks

    # 상어가 이동한다
    # 이동을 마친 후 한 칸에 상어가 두 마리 이상 있는 경우 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다
    temp = [[[]] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if sharks[i][j]:
                direction, speed, weight = sharks[i][j]
                s = speed
                # 1: 위 # 2: 아래 # 3: 오른쪽 # 4: 왼쪽
                if speed == 0:  # 이동하지 않는 상어인 경우
                    if not temp[i][j] or temp[i][j][2] < weight:
                        temp[i][j] = [direction, speed, weight]

                elif direction == 1 or direction == 2:  # 위쪽 or 아래쪽으로 이동하던 상어인 경우
                    cycle = R * 2 - 2  # 0 1 2 3 2 1 0
                    if direction == 1:
                        s += 2 * (R - 1) - i
                    else:
                        s += i

                    s %= cycle
                    index = s
                    direction = 2

                    if s >= R:
                        index = 2 * R - 2 - s
                        direction = 1

                    if not temp[index][j] or temp[index][j][2] < weight:
                        temp[index][j] = [direction, speed, weight]

                else:  # 오른쪽 or 왼쪽으로 이동하던 상어인 경우
                    cycle = C * 2 - 2
                    if direction == 4:
                        s += 2 * (C - 1) - j
                    else:
                        s += j

                    s %= cycle
                    index = s
                    direction = 3

                    if s >= C:
                        index = 2 * C - 2 - s
                        direction = 4

                    if not temp[i][index] or temp[i][index][2] < weight:
                        temp[i][index] = [direction, speed, weight]

    sharks = temp


total_size = 0

for i in range(C):
    # 낚시왕이 오른쪽으로 한 칸 이동한다
    total_size += fishing(i)

    if i == C - 1:
        break

    swim()

print(total_size)
