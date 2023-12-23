# 연구소
import collections

row, col = map(int, input().split())
laboratory = [[*map(int, input().split())] for _ in range(row)]


def find_safe_area():
    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]

    visited = [[False] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if laboratory[i][j] == 1:
                visited[i][j] = True

            elif laboratory[i][j] == 2 and not visited[i][j]:
                queue = collections.deque([(i, j)])
                visited[i][j] = True

                while queue:
                    r, c = queue.popleft()

                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < row and 0 <= nc < col:
                            if not visited[nr][nc]:
                                if laboratory[nr][nc] == 0 or laboratory[nr][nc] == 2:
                                    queue.append((nr, nc))
                                visited[nr][nc] = True

    return row * col - sum(map(sum, visited))


def combination(array):
    answer = [0]

    def generate(index, temp):
        if len(temp) == 3:
            for r, c in temp:
                laboratory[r][c] = 1

            answer[0] = max(answer[0], find_safe_area())

            for r, c in temp:
                laboratory[r][c] = 0

            return

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i + 1, temp)
            temp.pop()

    generate(0, [])

    return answer[0]


empty = []

for i in range(row):
    for j in range(col):
        if laboratory[i][j] == 0:
            empty.append([i, j])

print(combination(empty))
