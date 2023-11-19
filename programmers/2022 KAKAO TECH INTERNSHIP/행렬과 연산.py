from collections import deque


def solution(rc, operations):
    lines = len(rc)

    left_col = deque([rc[i][0] for i in range(lines)])
    right_col = deque([rc[i][-1] for i in range(lines)])
    rows = deque([deque(rc[i][1:-1]) for i in range(lines)])

    for operation in operations:
        if operation == "Rotate":
            rows[-1].append(right_col.pop())
            left_col.append(rows[-1].popleft())
            rows[0].appendleft(left_col.popleft())
            right_col.appendleft(rows[0].pop())
        else:  # ShiftRow
            left_col.appendleft(left_col.pop())
            right_col.appendleft(right_col.pop())
            rows.appendleft(rows.pop())

    answer = []

    for i in range(lines):
        answer.append([left_col[i]] + list(rows[i]) + [right_col[i]])

    return answer
