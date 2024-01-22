from collections import deque

BLOCKS = [
    {(0, 0), (1, 0), (1, 1), (1, 2)},
    {(0, 1), (1, 1), (2, 0), (2, 1)},
    {(0, 0), (1, 0), (2, 0), (2, 1)},
    {(0, 2), (1, 0), (1, 1), (1, 2)},
    {(0, 1), (1, 0), (1, 1), (1, 2)},
]


def extract_block(r, c, visited, board):
    n = len(visited)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[r][c] = True

    block = [[r, c]]
    block_type = board[r][c]
    queue = deque([(r, c)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == block_type:
                    visited[nx][ny] = True
                    block.append([nx, ny])
                    queue.append((nx, ny))

    return block


def is_removable(block, board):
    minX = min([x for x, y in block])
    minY = min([y for x, y in block])
    standard_block = set([(x - minX, y - minY) for x, y in block])

    if standard_block in BLOCKS:
        if not is_blind(block, board):
            return True

    return False


def is_blind(block, board):
    blockY = [y for x, y in block]
    checkY = [[x, y] for x, y in block if blockY.count(y) == 1]

    for x, y in checkY:
        x -= 1
        while 0 <= x:
            if 0 != board[x][y]:
                return True
            x -= 1

    return False


def remove_block(block, board):
    for x, y in block:
        board[x][y] = 0


def check_board(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]

    result = 0

    for row in range(n):
        for col in range(n):
            if board[row][col] != 0 and not visited[row][col]:
                block = extract_block(row, col, visited, board)

                if is_removable(block, board):
                    result += 1
                    remove_block(block, board)

    return result


def solution(board):
    answer = 0

    while True:
        removed = check_board(board)

        if not removed:
            break

        answer += removed

    return answer
