# 부분합
N, S = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
prefix_sum = [0] + [0] * N

left = 0
right = 1
answer = 100000

while N >= right >= left:
    prefix_sum[right] = numbers[right] + prefix_sum[right - 1]

    if numbers[right] >= S:
        answer = 1

        right += 1
        left = right
    elif prefix_sum[right] >= S:
        while left + 1 < right and prefix_sum[right] - prefix_sum[left + 1] >= S:
            left += 1

        answer = min(answer, right - left if right - left > 0 else 1)
        right += 1
    else:
        right += 1

print(answer if answer < 100000 else 0)
