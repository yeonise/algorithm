# 버블 소트

N = int(input())
numbers = list(map(int, input().split()))


def merge_sort(start, end):
    if start == end:
        return 0

    mid = (start + end) // 2

    answer = merge_sort(start, mid) + merge_sort(mid + 1, end)

    result = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if numbers[left] <= numbers[right]:
            result.append(numbers[left])
            left += 1
        else:
            result.append(numbers[right])
            right += 1
            answer += mid - left + 1

    while left <= mid:
        result.append(numbers[left])
        left += 1

    while right <= end:
        result.append(numbers[right])
        right += 1

    for i in range(start, end + 1):
        numbers[i] = result[i - start]

    return answer


print(merge_sort(0, N - 1))
