n = int(input())

landmine = [list(input()) for _ in range(n)]
game_map = [list(input()) for _ in range(n)]

count = [[0] * n for _ in range(n)]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]

for row in range(n):
    for col in range(n):

        if landmine[row][col] == '*':
            for k in range(8):
                ny = row + dy[k]
                nx = col + dx[k]

                if 0 <= ny < n and 0 <= nx < n:
                    count[ny][nx] += 1

flag = False

for row in range(n):
    for col in range(n):

        if game_map[row][col] == 'x':
            game_map[row][col] = count[row][col]

            if landmine[row][col] == '*':
                flag = True

if flag:
    for row in range(n):
        for col in range(n):

            if landmine[row][col] == '*':
                game_map[row][col] = '*'

for line in game_map:
    line = list(map(str, line))
    print(''.join(line))
