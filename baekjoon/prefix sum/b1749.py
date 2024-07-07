# 점수 따먹기
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
puzzle = [list(map(int, read().split())) for _ in range(N)]

answer = -10000

for i in range(N):
    p = [0] * M  # 각 열의 누적합 p
    for j in range(i, N):
        t = [0] * M  # 범위 내에서의 최대 부분합
        for k in range(M):
            p[k] += puzzle[j][k]
            if k > 0:
                t[k] = max(t[k - 1] + p[k], p[k])
            else:
                t[k] = p[k]

            answer = max(t[k], answer)

print(answer)
