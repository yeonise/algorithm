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


# 예시 배열
arr = [1, 2, 4, 4, 4, 6, 7]

# Lower Bound와 Upper Bound 예시
target_value = 4
lower_bound_index = lower_bound(arr, target_value)
upper_bound_index = upper_bound(arr, target_value)

# 결과 출력
print(f"Lower Bound of {target_value}: {lower_bound_index}")
print(f"Upper Bound of {target_value}: {upper_bound_index}")

# 출력 결과
# Lower Bound of 4: 2
# Upper Bound of 4: 5
