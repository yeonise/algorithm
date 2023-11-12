import collections


def solution(board):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    UNVISITED = 25 * 25 * 6
    START = -1

    width = len(board)
    distance = [[[UNVISITED] * 4 for _ in range(width)] for _ in range(width)]

    queue = collections.deque()
    queue.append((0, 0, START))
    for i in range(4):
        distance[0][0][i] = 0

    while queue:
        x, y, direction = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < width and 0 <= ny < width:
                if board[nx][ny] != 1:
                    if (direction == START) or (i == direction and distance[nx][ny][i] > distance[x][y][i] + 1):
                        distance[nx][ny][i] = distance[x][y][i] + 1
                        queue.append((nx, ny, i))
                    elif i != direction and distance[nx][ny][i] > distance[x][y][direction] + 6:
                        distance[nx][ny][i] = distance[x][y][direction] + 6
                        queue.append((nx, ny, i))

    return min(distance[-1][-1]) * 100
