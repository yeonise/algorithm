# 준표의 조약돌
N, B, W = map(int, input().split())
pebbles = input()

B_count = 0
W_count = 0
left = 0
right = 0
answer = 0

while right < N:
    if pebbles[right] == 'B':
        B_count += 1
    else:
        W_count += 1

    while B_count > B:
        if pebbles[left] == 'B':
            B_count -= 1
        else:
            W_count -= 1
        left += 1

    if W_count >= W:
        answer = max(answer, right - left + 1)

    if left > right:
        right = left
    else:
        right += 1

print(answer)
