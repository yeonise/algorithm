def solution(a):
    # 더 큰 풍선만을 터트리다보면 항상 가장 작은 숫자의 풍선이 마지막에 남는다
    left_min = [a[0]]
    for i in range(1, len(a)):
        left_min.append(min(left_min[-1], a[i]))

    right_min = [a[-1]]
    for i in range(len(a) - 2, -1, -1):
        right_min.append(min(right_min[-1], a[i]))

    answer = 0
    for i in range(len(a)):
        if a[i] <= right_min.pop() or a[i] <= left_min[i]:
            answer += 1

    return answer
