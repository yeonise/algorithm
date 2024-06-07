# 팀 빌딩
N = int(input())
ability = list(map(int, input().split()))
left = 0
right = N - 1
synergy = (right - left - 1) * min(ability[left], ability[right])

while left < right:
    between = right - left - 1
    min_ability = min(ability[left], ability[right])
    synergy = max(synergy, between * min_ability)

    left_is_smaller = ability[left] < ability[right]
    if left_is_smaller:
        left += 1
    else:
        right -= 1

print(synergy)
