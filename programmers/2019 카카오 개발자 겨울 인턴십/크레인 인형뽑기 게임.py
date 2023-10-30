def solution(board, moves):
    column_size = len(board[0])
    row_size = len(board)
    replaced_board = [[] for _ in range(column_size)]

    for i in range(row_size - 1, -1, -1):
        for j in range(column_size):
            type = board[i][j]

            if type != 0:
                replaced_board[j].append(type)

    basket = []
    pop_count = 0

    for line in moves:
        target_line = replaced_board[line - 1]

        if target_line:
            doll = target_line.pop()

            if basket and basket[-1] == doll:
                basket.pop()
                pop_count += 2
            else:
                basket.append(doll)

    return pop_count
