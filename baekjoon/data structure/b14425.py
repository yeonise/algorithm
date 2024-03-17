# 문자열 집합
import sys

read = sys.stdin.readline
N, M = map(int, read().split())

dictionary = set()

for _ in range(N):
    dictionary.add(read())

answer = 0
for _ in range(M):
    if read() in dictionary:
        answer += 1

print(answer)
