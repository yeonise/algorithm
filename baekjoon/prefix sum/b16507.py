# 어두운 건 무서워
import sys

read = sys.stdin.readline

R, C, Q = map(int, read().split())  # 사진의 크기와 테스트 개수
photo = [[0] * (C + 2)]

for _ in range(R):
    photo.append([0] + list(map(int, read().split())))

for row in range(1, R + 1):
    for col in range(1, C + 1):
        photo[row][col] += photo[row][col - 1]

for col in range(1, C + 1):
    for row in range(1, R + 1):
        photo[row][col] += photo[row - 1][col]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, read().split())
    width = c2 - c1 + 1
    height = r2 - r1 + 1

    total_light = photo[r2][c2] - photo[r2][c1 - 1] - photo[r1 - 1][c2] + photo[r1 - 1][c1 - 1]

    print(total_light // (width * height))
