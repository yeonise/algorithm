# 모기야 오지마
import sys
from collections import defaultdict

read = sys.stdin.readline

N = int(read())  # 방에 출입한 모기의 수
dictionary = defaultdict(int)

for _ in range(N):
    i, o = map(int, read().split())
    dictionary[i] += 1
    dictionary[o] -= 1

answer = 0
mosquito = 0
start = 0
end = 0
is_max = False

for time in sorted(dictionary.keys()):
    mosquito += dictionary[time]

    if mosquito > answer:
        answer = mosquito
        start = time
        is_max = True
    elif is_max and mosquito < answer and mosquito - dictionary[time] == answer:
        end = time
        is_max = False

print(answer)
print(start, end)
