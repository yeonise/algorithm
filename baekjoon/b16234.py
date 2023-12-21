# 인구 이동
import collections

N, L, R = map(int, input().split())
land = [[*map(int, input().split())] for _ in range(N)]


def bfs(row, col):
    connected = set()  # 연결된 땅
    people = 0  # 총 인구 수
    queue = collections.deque([[row, col]])
    visited[row][col] = True

    while queue:
        r, c = queue.popleft()
        people += land[r][c]
        connected.add((r, c))

        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]

            if 0 <= nr < N and 0 <= nc < N:
                if opened[nr][nc] and not visited[nr][nc]:
                    if L <= abs(land[r][c] - land[nr][nc]) <= R:
                        queue.append([nr, nc])
                        visited[nr][nc] = True

    moved_result = people // len(connected)

    for lr, lc in connected:
        land[lr][lc] = moved_result

    return len(connected) > 1


flag = True
days = 0

while flag:
    today = False
    opened = [[False] * N for _ in range(N)]  # 개방 여부 표시

    # 국경선 개방 여부 결정하기
    # 오른쪽과 아래만 확인하면 된다
    for i in range(N):
        for j in range(N):
            # 아래 확인하기
            if i + 1 < N:
                if L <= abs(land[i][j] - land[i + 1][j]) <= R:
                    opened[i][j] = True
                    opened[i + 1][j] = True
            # 오른쪽 확인하기
            if j + 1 < N:
                if L <= abs(land[i][j] - land[i][j + 1]) <= R:
                    opened[i][j] = True
                    opened[i][j + 1] = True

    # 연결된 땅 탐색하기
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if opened[i][j] and not visited[i][j]:
                if bfs(i, j):
                    today = True
    if today:
        days += 1

    flag = today

print(days)
