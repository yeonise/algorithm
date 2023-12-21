# 나무 재테크

# r과 c는 1부터 시작한다
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다

# = 봄 =
# 나무가 있는 칸에 있는 양분만 먹을 수 있다
# 나무는 자신의 나이만큼 양분을 먹는다
# 하나의 칸에 여러 개의 나무가 있다면 나이가 어린 나무부터 양분을 먹는다
# 땅에 양분이 부족해 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽는다
def spring():
    food_by_tree = []

    for i in range(N):
        for j in range(N):
            tree_ages = trees[i][j]

            if not tree_ages:
                continue

            tree_ages.sort(reverse=True)
            alive = []

            while tree_ages and food[i][j] > 0 and food[i][j] >= tree_ages[-1]:
                current_tree = tree_ages.pop()
                food[i][j] -= current_tree
                alive.append(current_tree + 1)

            total_food = 0
            for age in tree_ages:
                total_food += age // 2

            if total_food > 0:
                food_by_tree.append([i, j, total_food])

            trees[i][j] = alive[:]

    return food_by_tree


# = 여름 =
# 죽은 나무는 양분으로 변한다
# 죽은 나무의 나이를 2로 나눈 값이 양분이 된다
# 소수점 아래는 버린다
def summer(food_by_dead_tree):
    for y, x, f in food_by_dead_tree:
        food[y][x] += f


# = 가을 =
# 나이가 5의 배수인 나무는 번식한다
# 인접한 8개의 칸에 나이가 1인 나무가 생긴다
def fall():
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            for tree_age in trees[i][j]:
                if tree_age % 5 == 0:
                    for di in range(8):
                        nx = j + dy[di]
                        ny = i + dx[di]

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[ny][nx].append(1)


# = 겨울 =
# 로봇이 땅에 양분을 추가한다
# 각 칸에 추가되는 양분의 양은 입력으로 주어진다
def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += robot_gives[i][j]


N, M, K = map(int, input().split())
robot_gives = [[*map(int, input().split())] for i in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
food = [[5] * N for _ in range(N)]

for _ in range(M):
    y, x, age = map(int, input().split())
    trees[y - 1][x - 1].append(age)

for _ in range(K):
    summer(spring())
    fall()
    winter()

answer = 0

for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
