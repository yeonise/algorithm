# 피아노 체조
import sys

read = sys.stdin.readline

N = int(read())  # 악보의 개수
difficulty = [0] + list(map(int, read().split()))  # 악보의 난이도
Q = int(read())  # 질문의 개수

mistake = [0] * (N + 1)

for index in range(1, N):
    do = difficulty[index] > difficulty[index + 1]
    mistake[index] = int(do) + mistake[index - 1]

mistake[N] = mistake[N - 1]

for _ in range(Q):
    x, y = map(int, read().split())
    answer = mistake[y] - mistake[x - 1]

    if y < N and difficulty[y] > difficulty[y + 1]:
        answer -= 1

    print(answer)
