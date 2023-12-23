# 뱀과 사다리 게임
import collections

N, M = map(int, input().split())  # 사다리의 수, 뱀의 수

move = {}
for _ in range(N + M):
    start, end = map(int, input().split())
    move[start] = end

queue = collections.deque([(1, 0)])  # 현재 위치, 주사위를 굴린 횟수
visited = [False] * 101
visited[1] = True

while queue:
    current, roll = queue.popleft()

    if current == 100:
        print(roll)
        break

    for i in range(1, 7):
        next = current + i

        if next <= 100 and not visited[next]:
            visited[next] = True

            if next in move:
                queue.append((move[next], roll + 1))
                visited[move[next]] = True
                continue

            queue.append((next, roll + 1))
