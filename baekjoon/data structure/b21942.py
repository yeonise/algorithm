# 부품 대여장
import sys
from collections import defaultdict

N, L, F = sys.stdin.readline().split()  # 대여장에 작성된 정보의 개수, 대여 기간, 벌금
N = int(N)
F = int(F)
L_day, L_time = L.split('/')
L_day = int(L_day) * (24 * 60)
L_hour, L_minute = map(int, L_time.split(':'))
L_time = L_hour * 60 + L_minute
L = L_day + L_time
calendar = {0: 0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
dictionary = {}
result = defaultdict(int)

for _ in range(N):  # 시간순으로 들어온다
    date, time, P, M = sys.stdin.readline().split()  # 빌린 시각, 부품 이름, 회원 닉네임

    _, month, day = map(int, date.split('-'))
    hour, minute = map(int, time.split(':'))
    date = calendar[month - 1] + day
    time = hour * 60 + minute

    key = P + '-' + M
    if key not in dictionary:
        dictionary[key] = date * (24 * 60) + time
    else:
        borrow_time = dictionary[key]
        period = (date * (24 * 60) + time) - borrow_time

        if period > L:
            fine = (period - L) * F
            result[M] += fine

        dictionary.pop(key)

if result:
    for name in sorted(result.keys()):
        print(name, result[name])
else:
    print(-1)
