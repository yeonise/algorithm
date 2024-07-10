# 개똥벌레
import sys

read = sys.stdin.readline

N, H = map(int, read().split())
hurdles = [int(read()) for _ in range(N)]

S = [0] * (H + 1)  # 석순
J = [0] * (H + 1)  # 종유석

for i in range(N):
    if i % 2 == 0:  # 석순인 경우
        S[hurdles[i]] += 1
    else:  # 종유석인 경우
        J[hurdles[i]] += 1

for i in range(H - 1, 0, -1):
    J[i] += J[i + 1]
    S[i] += S[i + 1]

min_hurdle_count = N
way_count = 0

for way in range(1, H + 1):
    hurdle_count = S[way] + J[H - way + 1]

    if min_hurdle_count > hurdle_count:
        min_hurdle_count = hurdle_count
        way_count = 1
    elif min_hurdle_count == hurdle_count:
        way_count += 1

print(min_hurdle_count, way_count)
