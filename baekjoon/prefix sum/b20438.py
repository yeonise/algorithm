# 출석체크
# N: 학생의 수
# K: 졸고 있는 학생의 수
# Q: 출석 코드를 보낼 학생의 수
# M: 주어질 구간의 수
import sys

read = sys.stdin.readline

N, K, Q, M = map(int, read().split())
sleep = set(map(int, read().split()))
code = list(map(int, read().split()))

students = [0] * (N + 3)

for number in code:
    if number in sleep:
        continue

    temp = number

    while temp < N + 3:
        if temp in sleep:
            temp += number
            continue

        students[temp] = 1
        temp += number

prefix_sum = [0] * (N + 3)

for i in range(3, N + 3):
    prefix_sum[i] = prefix_sum[i - 1] + students[i]

for _ in range(M):
    start, end = map(int, read().split())

    print((end - start + 1) - (prefix_sum[end] - prefix_sum[start - 1]))
