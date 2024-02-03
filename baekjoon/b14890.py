# 경사로

import sys

N, L = map(int, sys.stdin.readline().split())
init_map = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]


def is_road(line):
    placed = [False] * len(line)  # 경사로 배치 여부

    for i in range(len(line) - 1):
        if line[i] != line[i + 1]:  # 해당 행에서 다른 높이를 갖는다면
            if abs(line[i] - line[i + 1] > 1):  # 연속된 땅의 높이의 차가 1보다 크다면 길이 될 수 없다
                return False
            if line[i] - line[i + 1] == 1:  # 왼쪽이 더 높고 오른쪽이 더 낮은 경우
                if i + L >= N:
                    return False

                temp = i + 1
                while temp <= i + L:
                    if line[temp] + 1 != line[i] or placed[temp]:
                        return False
                    placed[temp] = True
                    temp += 1
            else:  # 오른쪽이 더 높고 왼쪽이 더 낮은 경우
                if i - L + 1 < 0:
                    return False
                temp = i
                while temp >= i - L + 1:
                    if line[temp] + 1 != line[i + 1] or placed[temp]:
                        return False
                    placed[temp] = True
                    temp -= 1

    return True


answer = 0

for i in range(N):
    answer += is_road(init_map[i])
    answer += is_road([init_map[row][i] for row in range(N)])

print(answer)
