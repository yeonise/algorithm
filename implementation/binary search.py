def lower_bound(arr, target):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


def upper_bound(arr, target):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid

    return low


# 이분 탐색이 원하는 값 k를 찾는 과정이라면
# Lower Bound는 원하는 값 k 이상이 처음 등장하는 위치를 찾는 과정이고
# Upper Bound는 원하는 값 k를 초과한 값이 처음 나오는 위치를 찾는 과정이다

# Lower Bound는 정렬된 배열에서 탐색값이 2개 이상 있는 경우 가장 앞에 위치한 탐색값을 의미한다
# ex. 1 - [2] - 2 - 2 - 2 - 2 - 8 - 9
# Upper Bound는 가장 뒤에 위치한 탐색값의 다음 위치를 의미한다
# ex. 1 - 2 - 2 - 2 - 2 - 2 - [8] - 9

# Lower Bound와 Upper Bound 예시
arr = [1, 2, 4, 4, 4, 6, 7]
target_value = 4
lower_bound_index = lower_bound(arr, target_value)
upper_bound_index = upper_bound(arr, target_value)

# 결과 출력
print(f"Lower Bound of {target_value}: {lower_bound_index}")
print(f"Upper Bound of {target_value}: {upper_bound_index}")

# 출력 결과
# Lower Bound of 4: 2
# Upper Bound of 4: 5
