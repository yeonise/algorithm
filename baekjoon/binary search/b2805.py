# 나무 자르기
N, M = map(int, input().split())  # 나무 수, 집으로 가져가려고 하는 나무의 길이
trees = list(map(int, input().split()))

low, high = 0, max(trees)

while low + 1 < high:  # low와 high 사이에 다른 칸이 존재하는가?
    mid = low + (high - low) // 2  # 항상 low < mid < high를 만족한다
    total = sum([tree - mid for tree in trees if tree >= mid])

    if total >= M:
        low = mid
    else:
        high = mid

print(low)
