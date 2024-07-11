# 소용돌이 에쁘게 출력하기
def spiral_value(x, y):
    n = max(abs(x), abs(y))
    max_val = (2*n + 1)**2
    if x == n:
        return max_val - (n - y)
    elif y == -n:
        return max_val - 2*n - (n - x)
    elif x == -n:
        return max_val - 4*n - (n + y)
    else:
        return max_val - 6*n - (n + x)


r1, c1, r2, c2 = map(int, input().split())

max_val = max(spiral_value(r1, c1), spiral_value(r1, c2), spiral_value(r2, c1), spiral_value(r2, c2))
max_len = len(str(max_val))

for i in range(r1, r2 + 1):
    row = []
    for j in range(c1, c2 + 1):
        row.append(str(spiral_value(i, j)).rjust(max_len))
    print(" ".join(row))


