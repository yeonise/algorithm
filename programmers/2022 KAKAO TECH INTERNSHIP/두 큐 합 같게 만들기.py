from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    count = 0

    for _ in range(len(queue1) * 4):
        if sum1 == sum2:
            return count

        if sum1 > sum2:
            number = queue1.popleft()
            queue2.append(number)
            sum1 -= number
            sum2 += number
        else:
            number = queue2.popleft()
            queue1.append(number)
            sum1 += number
            sum2 -= number

        count += 1

    return -1


# 이때, 전체 배열의 길이가 2n이므로,
# 한 포인터 당 최대 2n번의 이동이 필요합니다.
# 따라서, 총 4n만큼의 작업을 수행한 뒤에도 두 큐의 합을 같게 만들지 못했다면
# 그 이후에는 이미 탐색했던 구간을 다시 탐색하는 것이므로 의미가 없습니다.

solution([1, 1, 1, 8, 10, 9], [1, 1, 1, 1, 1, 1])
