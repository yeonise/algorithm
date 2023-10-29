def solution(rows, columns, queries):
    box = []

    for r in range(1, rows + 1):
        box.append([number for number in range(1 + columns * (r - 1), (columns) * r + 1)])

    def rotate(query):
        up_r, up_c, down_r, down_c = query
        up_r -= 1
        up_c -= 1
        down_r -= 1
        down_c -= 1

        min_number = box[up_r][up_c]
        previous = box[up_r][up_c]

        # 왼쪽에서 오른쪽
        for column in range(up_c + 1, down_c + 1):
            box[up_r][column], previous = previous, box[up_r][column]
            min_number = min(min_number, previous)

        # 위에서 아래
        for row in range(up_r + 1, down_r + 1):
            box[row][down_c], previous = previous, box[row][down_c]
            min_number = min(min_number, previous)

        # 오른쪽에서 왼쪽
        for column in range(down_c - 1, up_c - 1, -1):
            box[down_r][column], previous = previous, box[down_r][column]
            min_number = min(min_number, previous)

        # 아래에서 위
        for row in range(down_r - 1, up_r - 1, -1):
            box[row][up_c], previous = previous, box[row][up_c]
            min_number = min(min_number, previous)

        return min_number

    answer = []

    for query in queries:
        answer.append(rotate(query))

    return answer
